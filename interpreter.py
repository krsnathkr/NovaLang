import math

from ast_nodes import (
    ProgramNode,
    NumberNode,
    BooleanNode,
    VariableNode,
    BinaryOpNode,
    UnaryOpNode,
    AssignmentNode,
    PrintNode,
    BlockNode,
    IfNode,
    WhileNode,
    FunctionDefNode,
    FunctionCallNode,
    ReturnNode,
)
from environment import Environment, UndefinedVariableError


class RuntimeErrorNova(RuntimeError):
    """Base class for NovaLang runtime errors."""


class DivisionByZeroError(RuntimeErrorNova):
    pass


class InvalidOperationError(RuntimeErrorNova):
    pass


class FunctionError(RuntimeErrorNova):
    pass


class ReturnSignal(Exception):
    """Internal signal used to return a value from a function."""

    def __init__(self, value):
        self.value = value


class NovaFunction:
    """Stores a NovaLang function definition and its defining environment."""

    def __init__(self, declaration, closure):
        self.declaration = declaration
        self.closure = closure

    def call(self, interpreter, arguments):
        parameters = self.declaration.parameters

        if len(arguments) != len(parameters):
            raise FunctionError(
                f"Function '{self.declaration.name}' expects "
                f"{len(parameters)} argument(s), but got {len(arguments)}"
            )

        # Every function call gets its own local environment.
        local_environment = Environment(self.closure)

        for parameter, value in zip(parameters, arguments):
            local_environment.define(parameter, value)

        previous_environment = interpreter.environment
        interpreter.environment = local_environment

        try:
            # Execute the function body directly in the function environment.
            # This keeps parameters and local variables in the same function scope.
            for statement in self.declaration.body.statements:
                interpreter.visit(statement)
        except ReturnSignal as signal:
            return signal.value
        finally:
            interpreter.environment = previous_environment

        return None


class Interpreter:
    """Tree-walking interpreter for NovaLang."""

    def __init__(self, environment=None):
        self.environment = environment or Environment()
        self.output = []
        self.function_depth = 0

    def execute(self, program):
        try:
            self.visit(program)
        except OverflowError:
            raise RuntimeErrorNova(
                "Numeric value is too large for this operation"
            ) from None
        return self.output

    def visit(self, node):
        method_name = "visit_" + type(node).__name__
        method = getattr(self, method_name, None)

        if method is None:
            raise RuntimeErrorNova(
                f"No interpreter rule for {type(node).__name__}"
            )

        return method(node)

    def visit_ProgramNode(self, node):
        for statement in node.statements:
            self.visit(statement)

    def visit_NumberNode(self, node):
        try:
            value = float(node.value) if "." in node.value else int(node.value)
        except ValueError:
            raise RuntimeErrorNova(
                f"Invalid numeric literal '{node.value}'"
            ) from None
        return self.check_numeric_range(value)

    def visit_BooleanNode(self, node):
        return node.value

    def visit_VariableNode(self, node):
        return self.environment.get(node.name)

    def visit_AssignmentNode(self, node):
        value = self.visit(node.value)

        if node.declaration:
            self.environment.define(node.name, value)
        else:
            self.environment.assign(node.name, value)

        return value

    def visit_PrintNode(self, node):
        value = self.visit(node.expression)
        text = self.format_value(value)

        self.output.append(text)
        print(text)

        return value

    def visit_BlockNode(self, node):
        previous = self.environment
        self.environment = Environment(previous)

        try:
            for statement in node.statements:
                self.visit(statement)
        finally:
            self.environment = previous

    def visit_IfNode(self, node):
        condition = self.visit(node.condition)

        self.require_boolean(
            condition,
            "if condition"
        )

        if condition:
            return self.visit(node.then_branch)

        if node.else_branch is not None:
            return self.visit(node.else_branch)

        return None

    def visit_WhileNode(self, node):
        while True:
            condition = self.visit(node.condition)

            self.require_boolean(
                condition,
                "while condition"
            )

            if not condition:
                break

            self.visit(node.body)

    # ---------------------------------------------------------
    # Part 5 - Functions
    # ---------------------------------------------------------

    def visit_FunctionDefNode(self, node):
        function = NovaFunction(
            node,
            self.environment
        )

        self.environment.define(
            node.name,
            function
        )

        return function

    def visit_FunctionCallNode(self, node):
        try:
            function = self.environment.get(node.name)
        except UndefinedVariableError:
            raise FunctionError(
                f"Undefined function '{node.name}'"
            ) from None

        if not isinstance(function, NovaFunction):
            raise FunctionError(
                f"'{node.name}' is not a function"
            )

        arguments = []

        for argument in node.arguments:
            arguments.append(
                self.visit(argument)
            )

        self.function_depth += 1

        try:
            return function.call(
                self,
                arguments
            )
        finally:
            self.function_depth -= 1

    def visit_ReturnNode(self, node):
        if self.function_depth == 0:
            raise FunctionError(
                "'return' can only be used inside a function"
            )

        value = self.visit(node.expression)

        raise ReturnSignal(value)

    # ---------------------------------------------------------
    # Operators
    # ---------------------------------------------------------

    def visit_UnaryOpNode(self, node):
        operand = self.visit(node.operand)

        if node.operator == "-":
            self.require_number(
                operand,
                "unary '-'"
            )
            return -operand

        if node.operator == "!":
            self.require_boolean(
                operand,
                "unary '!'"
            )
            return not operand

        raise InvalidOperationError(
            f"Unsupported unary operator '{node.operator}'"
        )

    def visit_BinaryOpNode(self, node):
        # Short-circuit logical AND.
        if node.operator == "&&":
            left = self.visit(node.left)

            self.require_boolean(
                left,
                "'&&'"
            )

            if not left:
                return False

            right = self.visit(node.right)

            self.require_boolean(
                right,
                "'&&'"
            )

            return left and right

        # Short-circuit logical OR.
        if node.operator == "||":
            left = self.visit(node.left)

            self.require_boolean(
                left,
                "'||'"
            )

            if left:
                return True

            right = self.visit(node.right)

            self.require_boolean(
                right,
                "'||'"
            )

            return left or right

        left = self.visit(node.left)
        right = self.visit(node.right)
        op = node.operator

        if op in {"+", "-", "*", "/", "%"}:
            self.require_number(
                left,
                f"'{op}'"
            )

            self.require_number(
                right,
                f"'{op}'"
            )

            if op in {"/", "%"} and right == 0:
                raise DivisionByZeroError(
                    "Division by zero"
                )

            if op == "+":
                result = left + right
            elif op == "-":
                result = left - right
            elif op == "*":
                result = left * right
            elif op == "/":
                result = left / right
            else:
                result = left % right
            return self.check_numeric_range(result)

        if op in {"<", ">", "<=", ">="}:
            self.require_number(
                left,
                f"'{op}'"
            )

            self.require_number(
                right,
                f"'{op}'"
            )

            if op == "<":
                return left < right

            if op == ">":
                return left > right

            if op == "<=":
                return left <= right

            if op == ">=":
                return left >= right

        if op in {"==", "!="}:
            if type(left) is not type(right) and not (
                self.is_number(left)
                and self.is_number(right)
            ):
                raise InvalidOperationError(
                    f"Cannot compare "
                    f"{self.type_name(left)} with "
                    f"{self.type_name(right)}"
                )

            if op == "==":
                return left == right

            return left != right

        raise InvalidOperationError(
            f"Unsupported binary operator '{op}'"
        )

    # ---------------------------------------------------------
    # Runtime helpers
    # ---------------------------------------------------------

    @staticmethod
    def check_numeric_range(value):
        if isinstance(value, float) and not math.isfinite(value):
            raise RuntimeErrorNova("Numeric value is too large for this operation")
        return value

    @staticmethod
    def is_number(value):
        return (
            isinstance(value, (int, float))
            and not isinstance(value, bool)
        )

    @classmethod
    def require_number(cls, value, operation):
        if not cls.is_number(value):
            raise InvalidOperationError(
                f"Operator {operation} requires numeric values"
            )

    @staticmethod
    def require_boolean(value, context):
        if not isinstance(value, bool):
            raise InvalidOperationError(
                f"{context} must evaluate to true or false"
            )

    @staticmethod
    def type_name(value):
        if isinstance(value, bool):
            return "boolean"

        if isinstance(value, (int, float)):
            return "number"

        return type(value).__name__

    @staticmethod
    def format_value(value):
        if isinstance(value, bool):
            return "true" if value else "false"

        try:
            return str(value)
        except ValueError:
            raise RuntimeErrorNova("Numeric value is too large to print") from None


def run_source(source):
    """Lex, parse, and execute a NovaLang source string."""

    from lexer import tokenize
    from parser import Parser

    tokens = tokenize(source)
    program = Parser(tokens).parse_program()

    return Interpreter().execute(program)


def run_file(path):
    from pathlib import Path

    return run_source(
        Path(path).read_text(encoding="utf-8")
    )


if __name__ == "__main__":
    # Keep the earlier entry point compatible with the integrated CLI.
    from main import main

    raise SystemExit(main())
