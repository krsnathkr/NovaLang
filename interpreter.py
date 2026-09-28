from ast_nodes import (
    ProgramNode, NumberNode, BooleanNode, VariableNode, BinaryOpNode,
    UnaryOpNode, AssignmentNode, PrintNode, BlockNode, IfNode, WhileNode,
)
from environment import Environment, UndefinedVariableError


class RuntimeErrorNova(RuntimeError):
    """Base class for NovaLang runtime errors."""


class DivisionByZeroError(RuntimeErrorNova):
    pass


class InvalidOperationError(RuntimeErrorNova):
    pass


class Interpreter:
    """Tree-walking interpreter for the Part 4 NovaLang features."""

    def __init__(self, environment=None):
        self.environment = environment or Environment()
        self.output = []

    def execute(self, program):
        self.visit(program)
        return self.output

    def visit(self, node):
        method_name = "visit_" + type(node).__name__
        method = getattr(self, method_name, None)
        if method is None:
            raise RuntimeErrorNova(f"No interpreter rule for {type(node).__name__}")
        return method(node)

    def visit_ProgramNode(self, node):
        for statement in node.statements:
            self.visit(statement)

    def visit_NumberNode(self, node):
        try:
            return float(node.value) if "." in node.value else int(node.value)
        except ValueError:
            raise RuntimeErrorNova(f"Invalid numeric literal '{node.value}'") from None

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
        self.require_boolean(condition, "if condition")
        if condition:
            return self.visit(node.then_branch)
        if node.else_branch is not None:
            return self.visit(node.else_branch)
        return None

    def visit_WhileNode(self, node):
        while True:
            condition = self.visit(node.condition)
            self.require_boolean(condition, "while condition")
            if not condition:
                break
            self.visit(node.body)

    def visit_UnaryOpNode(self, node):
        operand = self.visit(node.operand)
        if node.operator == "-":
            self.require_number(operand, "unary '-'")
            return -operand
        if node.operator == "!":
            self.require_boolean(operand, "unary '!'")
            return not operand
        raise InvalidOperationError(f"Unsupported unary operator '{node.operator}'")

    def visit_BinaryOpNode(self, node):
        # Short-circuit logical operators.
        if node.operator == "&&":
            left = self.visit(node.left)
            self.require_boolean(left, "'&&'")
            if not left:
                return False
            right = self.visit(node.right)
            self.require_boolean(right, "'&&'")
            return left and right

        if node.operator == "||":
            left = self.visit(node.left)
            self.require_boolean(left, "'||'")
            if left:
                return True
            right = self.visit(node.right)
            self.require_boolean(right, "'||'")
            return left or right

        left = self.visit(node.left)
        right = self.visit(node.right)
        op = node.operator

        if op in {"+", "-", "*", "/", "%"}:
            self.require_number(left, f"'{op}'")
            self.require_number(right, f"'{op}'")
            if op in {"/", "%"} and right == 0:
                raise DivisionByZeroError("Division by zero")
            if op == "+":
                return left + right
            if op == "-":
                return left - right
            if op == "*":
                return left * right
            if op == "/":
                return left / right
            if op == "%":
                return left % right

        if op in {"<", ">", "<=", ">="}:
            self.require_number(left, f"'{op}'")
            self.require_number(right, f"'{op}'")
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
                self.is_number(left) and self.is_number(right)
            ):
                raise InvalidOperationError(
                    f"Cannot compare {self.type_name(left)} with {self.type_name(right)}"
                )
            return left == right if op == "==" else left != right

        raise InvalidOperationError(f"Unsupported binary operator '{op}'")

    @staticmethod
    def is_number(value):
        return isinstance(value, (int, float)) and not isinstance(value, bool)

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
        return str(value)


def run_source(source):
    """Lex, parse, and execute a NovaLang source string."""
    from lexer import tokenize
    from parser import Parser

    tokens = tokenize(source)
    program = Parser(tokens).parse_program()
    return Interpreter().execute(program)


def run_file(path):
    from pathlib import Path
    return run_source(Path(path).read_text(encoding="utf-8"))


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        raise SystemExit("Usage: python3 interpreter.py <program-file>")

    try:
        run_file(sys.argv[1])
    except (OSError, UnicodeError, UndefinedVariableError,
            DivisionByZeroError, InvalidOperationError, RuntimeErrorNova) as error:
        print(f"Runtime error: {error}", file=sys.stderr)
        raise SystemExit(1) from None
