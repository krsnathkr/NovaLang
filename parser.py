from ast_nodes import (
    ProgramNode,
    NumberNode,
    VariableNode,
    BinaryOpNode,
    UnaryOpNode,
    AssignmentNode,
    PrintNode,
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
        if self.current >= len(self.tokens):
            return None

        return self.tokens[self.current]

    def advance(self):
        token = self.peek()

        if token is not None:
            self.current += 1

        return token

    def check(self, token_type):
        token = self.peek()

        if token is None:
            return False

        return token.type == token_type

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

    def parse_primary(self):
        token = self.peek()

        if token is None:
            raise ParseError("Expected expression")

        # Number
        if self.check("NUMBER"):
            token = self.advance()
            return NumberNode(token.lexeme)

        # Identifier
        if self.check("ID"):
            token = self.advance()
            return VariableNode(token.lexeme)

        # Parenthesized expression
        if self.match("LPAREN"):
            expression = self.parse_expression()
            self.expect(
                "RPAREN",
                "Expected ')' after expression"
            )
            return expression

        raise ParseError(
            f"Expected expression, found '{token.lexeme}'",
            token
        )

    def parse_unary(self):
        if self.match("MINUS"):
            operand = self.parse_unary()
            return UnaryOpNode("-", operand)

        return self.parse_primary()


    def parse_term(self):
        expression = self.parse_unary()

        while self.check("STAR") or self.check("SLASH") or self.check("PERCENT"):
            operator = self.advance()
            right = self.parse_unary()

            expression = BinaryOpNode(
                operator.lexeme,
                expression,
                right
            )

        return expression


    def parse_expression(self):
        expression = self.parse_term()

        while self.check("PLUS") or self.check("MINUS"):
            operator = self.advance()
            right = self.parse_term()

            expression = BinaryOpNode(
                operator.lexeme,
                expression,
                right
            )

        return expression

    def parse_statement(self):
        if self.match("LET"):
            return self.parse_variable_declaration()

        if self.check("ID"):
            return self.parse_assignment()

        if self.match("PRINT"):
            return self.parse_print_statement()

        raise ParseError(
            f"Unexpected token '{self.peek().lexeme}'",
            self.peek()
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
            name=name.lexeme,
            value=value,
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
            name=name.lexeme,
            value=value
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

    def parse_program(self):
        statements = []

        while self.peek() is not None:
            statements.append(self.parse_statement())

        return ProgramNode(statements)