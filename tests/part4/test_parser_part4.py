import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from lexer import tokenize
from parser import Parser


def parse(source):
    return Parser(tokenize(source)).parse_program()


def test_comparison():
    ast = parse("let x = 10; if (x >= 10) { print(x); }")
    output = ast.pretty()
    assert "IfNode" in output
    assert "BinaryOpNode(>=)" in output


def test_if_else():
    ast = parse("if (1 < 2) { print(1); } else { print(0); }")
    output = ast.pretty()
    assert "IfNode" in output
    assert "Then" in output
    assert "Else" in output


def test_while():
    ast = parse("let x = 1; while (x <= 5) { x = x + 1; }")
    output = ast.pretty()
    assert "WhileNode" in output
    assert "BinaryOpNode(<=)" in output


if __name__ == "__main__":
    test_comparison()
    test_if_else()
    test_while()
    print("All Part 4 parser/control tests passed!")
