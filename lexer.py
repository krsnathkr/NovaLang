"""Tokenize NovaLang source according to the Part 1 EBNF grammar."""

from dataclasses import dataclass
from pathlib import Path
import re
import sys


KEYWORDS = {
    "let": "LET",
    "print": "PRINT",
    "if": "IF",
    "else": "ELSE",
    "while": "WHILE",
    "fn": "FN",
    "return": "RETURN",
    "true": "TRUE",
    "function": "FUNCTION",
    "false": "FALSE",
}

TWO_CHAR_TOKENS = {
    "==": "EQUAL_EQUAL",
    "!=": "BANG_EQUAL",
    "<=": "LESS_EQUAL",
    ">=": "GREATER_EQUAL",
    "&&": "AND_AND",
    "||": "OR_OR",
}

ONE_CHAR_TOKENS = {
    "+": "PLUS",
    "-": "MINUS",
    "*": "STAR",
    "/": "SLASH",
    "%": "PERCENT",
    "<": "LESS",
    ">": "GREATER",
    "!": "BANG",
    "=": "ASSIGN",
    "(": "LPAREN",
    ")": "RPAREN",
    "{": "LBRACE",
    "}": "RBRACE",
    ",": "COMMA",
    ";": "SEMICOLON",
}

IDENTIFIER = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")
NUMBER = re.compile(r"[0-9]+(?:\.[0-9]+)?")


@dataclass(frozen=True)
class Token:
    type: str
    lexeme: str
    line: int
    column: int

    def __str__(self) -> str:
        if self.type in {"ID", "NUMBER"}:
            return f"{self.type}({self.lexeme})"
        return self.type


class LexicalError(ValueError):
    """An invalid source character or malformed numeric literal."""

    def __init__(self, message: str, line: int, column: int):
        self.line = line
        self.column = column
        super().__init__(f"Lexical error at line {line}, column {column}: {message}")


def tokenize(source: str) -> list[Token]:
    """Return source-order tokens, skipping whitespace and rejecting invalid text."""
    tokens = []
    position = 0
    line = 1
    column = 1

    while position < len(source):
        char = source[position]
        if char.isspace():
            if char == "\n" or (
                char == "\r" and source[position:position + 2] != "\r\n"
            ):
                line += 1
                column = 1
            else:
                column += 1
            position += 1
            continue

        start_line, start_column = line, column
        if match := IDENTIFIER.match(source, position):
            lexeme = match.group()
            token_type = KEYWORDS.get(lexeme, "ID")
        elif match := NUMBER.match(source, position):
            lexeme = match.group()
            following = source[match.end():match.end() + 1]
            if following == "." or (
                following
                and following.isascii()
                and (following.isalpha() or following == "_")
            ):
                invalid_start = source[position:match.end() + 1]
                raise LexicalError(f"invalid number near {invalid_start!r}", line, column)
            token_type = "NUMBER"
        else:
            lexeme = source[position:position + 2]
            token_type = TWO_CHAR_TOKENS.get(lexeme)
            if token_type is None:
                lexeme = char
                token_type = ONE_CHAR_TOKENS.get(char)
            if token_type is None:
                raise LexicalError(f"invalid character {char!r}", line, column)

        tokens.append(Token(token_type, lexeme, start_line, start_column))
        position += len(lexeme)
        column += len(lexeme)

    return tokens


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python3 lexer.py <program-file>")
    try:
        for token in tokenize(Path(sys.argv[1]).read_text(encoding="utf-8")):
            print(token)
    except (OSError, UnicodeError, LexicalError) as error:
        print(error, file=sys.stderr)
        raise SystemExit(1) from None
