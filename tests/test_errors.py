import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from lexer import tokenize
from parser import Parser, ParseError


def check_error(source, description):
    try:
        tokens = tokenize(source)
        parser = Parser(tokens)
        parser.parse_program()

        print(f"FAIL: {description}")

    except ParseError as error:
        print(f"PASS: {description}")
        print(f"      {error}")


check_error(
    "let x = ;",
    "Missing expression in declaration"
)

check_error(
    "let = 10;",
    "Missing variable name"
)

check_error(
    "x = ;",
    "Missing expression in assignment"
)

check_error(
    "print();",
    "Missing print expression"
)

check_error(
    "print(10;",
    "Missing closing parenthesis"
)

check_error(
    "let x = 10",
    "Missing semicolon"
)