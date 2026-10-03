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


class ParseError(Exception):
    """Raised when NovaLang source contains invalid syntax."""

    def __init__(self, message, token=None):
        if token is not None:
            message = (
                f"Parse error at line {token.line}, "
                f"column {token.column}: {message}"
            )
        super().__init__(message)


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def peek(self):
        return self.tokens[self.current] if self.current < len(self.tokens) else None

    def peek_next(self):
        next_index = self.current + 1
        return self.tokens[next_index] if next_index < len(self.tokens) else None

    def advance(self):
        token = self.peek()
        if token is not None:
            self.current += 1
        return token

    def check(self, token_type):
        token = self.peek()
        return token is not None and token.type == token_type

    def match(self, *token_types):
        for token_type in token_types:
            if self.check(token_type):
                return self.advance()
        return None

    def expect(self, token_type, message=None):
        if self.check(token_type):
            return self.advance()

        token = self.peek()

        if message is None:
            message = f"Expected {token_type}"

        raise ParseError(message, token)

    # ---------------------------------------------------------
    # Expressions
    # ---------------------------------------------------------

    def parse_primary(self):
        token = self.peek()

        if token is None:
            raise ParseError("Expected expression")

        if self.check("NUMBER"):
            return NumberNode(self.advance().lexeme)

        if self.match("TRUE"):
            return BooleanNode(True)

        if self.match("FALSE"):
            return BooleanNode(False)

        if self.check("ID"):
            name = self.advance().lexeme

            # Function call
            if self.match("LPAREN"):
                arguments = []

                if not self.check("RPAREN"):
                    arguments.append(self.parse_expression())

                    while self.match("COMMA"):
                        arguments.append(self.parse_expression())

                self.expect("RPAREN", "Expected ')' after function arguments")

                return FunctionCallNode(name, arguments)

            # Normal variable
            return VariableNode(name)

        if self.match("LPAREN"):
            expression = self.parse_expression()
            self.expect("RPAREN", "Expected ')' after expression")
            return expression

        raise ParseError(
            f"Expected expression, found '{token.lexeme}'",
            token
        )

    def parse_unary(self):
        if self.match("MINUS"):
            return UnaryOpNode("-", self.parse_unary())

        if self.match("BANG"):
            return UnaryOpNode("!", self.parse_unary())

        return self.parse_primary()

    def parse_term(self):
        expression = self.parse_unary()

        while (
            self.check("STAR")
            or self.check("SLASH")
            or self.check("PERCENT")
        ):
            operator = self.advance()

            expression = BinaryOpNode(
                operator.lexeme,
                expression,
                self.parse_unary()
            )

        return expression

    def parse_additive(self):
        expression = self.parse_term()

        while self.check("PLUS") or self.check("MINUS"):
            operator = self.advance()

            expression = BinaryOpNode(
                operator.lexeme,
                expression,
                self.parse_term()
            )

        return expression

    def parse_comparison(self):
        expression = self.parse_additive()

        while (
            self.check("LESS")
            or self.check("GREATER")
            or self.check("LESS_EQUAL")
            or self.check("GREATER_EQUAL")
        ):
            operator = self.advance()

            expression = BinaryOpNode(
                operator.lexeme,
                expression,
                self.parse_additive()
            )

        return expression

    def parse_equality(self):
        expression = self.parse_comparison()

        while self.check("EQUAL_EQUAL") or self.check("BANG_EQUAL"):
            operator = self.advance()

            expression = BinaryOpNode(
                operator.lexeme,
                expression,
                self.parse_comparison()
            )

        return expression

    def parse_logical_and(self):
        expression = self.parse_equality()

        while self.check("AND_AND"):
            operator = self.advance()

            expression = BinaryOpNode(
                operator.lexeme,
                expression,
                self.parse_equality()
            )

        return expression

    def parse_logical_or(self):
        expression = self.parse_logical_and()

        while self.check("OR_OR"):
            operator = self.advance()

            expression = BinaryOpNode(
                operator.lexeme,
                expression,
                self.parse_logical_and()
            )

        return expression

    def parse_expression(self):
        return self.parse_logical_or()

    # ---------------------------------------------------------
    # Statements
    # ---------------------------------------------------------

    def parse_statement(self):
        if self.match("LET"):
            return self.parse_variable_declaration()

        if self.match("PRINT"):
            return self.parse_print_statement()

        if self.match("IF"):
            return self.parse_if_statement()

        if self.match("WHILE"):
            return self.parse_while_statement()

        if self.match("FUNCTION"):
            return self.parse_function_definition()

        if self.match("RETURN"):
            return self.parse_return_statement()

        if self.check("ID"):
            next_token = self.peek_next()

            # Assignment
            if next_token is not None and next_token.type == "ASSIGN":
                return self.parse_assignment()

            # Function call used as a statement
            expression = self.parse_expression()
            self.expect("SEMICOLON", "Expected ';' after function call")
            return expression

        token = self.peek()

        if token is None:
            raise ParseError("Expected statement")

        raise ParseError(
            f"Unexpected token '{token.lexeme}'",
            token
        )

    def parse_variable_declaration(self):
        name = self.expect(
            "ID",
            "Expected variable name after 'let'"
        )

        self.expect(
            "ASSIGN",
            "Expected '=' after variable name"
        )

        value = self.parse_expression()

        self.expect(
            "SEMICOLON",
            "Expected ';' after variable declaration"
        )

        return AssignmentNode(
            name.lexeme,
            value,
            declaration=True
        )

    def parse_assignment(self):
        name = self.expect(
            "ID",
            "Expected variable name"
        )

        self.expect(
            "ASSIGN",
            "Expected '=' after variable name"
        )

        value = self.parse_expression()

        self.expect(
            "SEMICOLON",
            "Expected ';' after assignment"
        )

        return AssignmentNode(
            name.lexeme,
            value
        )

    def parse_print_statement(self):
        self.expect(
            "LPAREN",
            "Expected '(' after 'print'"
        )

        expression = self.parse_expression()

        self.expect(
            "RPAREN",
            "Expected ')' after print expression"
        )

        self.expect(
            "SEMICOLON",
            "Expected ';' after print statement"
        )

        return PrintNode(expression)

    # ---------------------------------------------------------
    # Blocks and control flow
    # ---------------------------------------------------------

    def parse_block(self):
        self.expect(
            "LBRACE",
            "Expected '{' to start block"
        )

        statements = []

        while not self.check("RBRACE"):
            if self.peek() is None:
                raise ParseError(
                    "Expected '}' before end of input"
                )

            statements.append(
                self.parse_statement()
            )

        self.expect(
            "RBRACE",
            "Expected '}' after block"
        )

        return BlockNode(statements)

    def parse_if_statement(self):
        self.expect(
            "LPAREN",
            "Expected '(' after 'if'"
        )

        condition = self.parse_expression()

        self.expect(
            "RPAREN",
            "Expected ')' after if condition"
        )

        then_branch = self.parse_block()

        else_branch = None

        if self.match("ELSE"):
            else_branch = self.parse_block()

        return IfNode(
            condition,
            then_branch,
            else_branch
        )

    def parse_while_statement(self):
        self.expect(
            "LPAREN",
            "Expected '(' after 'while'"
        )

        condition = self.parse_expression()

        self.expect(
            "RPAREN",
            "Expected ')' after while condition"
        )

        body = self.parse_block()

        return WhileNode(
            condition,
            body
        )

    # ---------------------------------------------------------
    # Part 5 - Functions
    # ---------------------------------------------------------

    def parse_function_definition(self):
        name = self.expect(
            "ID",
            "Expected function name after 'function'"
        )

        self.expect(
            "LPAREN",
            "Expected '(' after function name"
        )

        parameters = []

        if not self.check("RPAREN"):
            parameter = self.expect(
                "ID",
                "Expected parameter name"
            )

            parameters.append(parameter.lexeme)

            while self.match("COMMA"):
                parameter = self.expect(
                    "ID",
                    "Expected parameter name after ','"
                )

                parameters.append(parameter.lexeme)

        self.expect(
            "RPAREN",
            "Expected ')' after parameters"
        )

        body = self.parse_block()

        return FunctionDefNode(
            name.lexeme,
            parameters,
            body
        )

    def parse_return_statement(self):
        expression = self.parse_expression()

        self.expect(
            "SEMICOLON",
            "Expected ';' after return value"
        )

        return ReturnNode(expression)

    # ---------------------------------------------------------
    # Program
    # ---------------------------------------------------------

    def parse_program(self):
        statements = []

        while self.peek() is not None:
            statements.append(
                self.parse_statement()
            )

        return ProgramNode(statements)