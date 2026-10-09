import contextlib
import io
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from interpreter import (
    Interpreter,
    run_source,
    DivisionByZeroError,
    InvalidOperationError,
)
from environment import UndefinedVariableError
from lexer import tokenize
from parser import Parser


def run_capture(source):
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        output = run_source(source)
    return output, buffer.getvalue().strip()


def check(name, source, expected):
    output, printed = run_capture(source)
    assert output == expected, f"{name}: expected {expected}, got {output}"
    assert printed.splitlines() == expected, f"{name}: console output mismatch"
    print(f"PASS: {name}")


def test_all():
    check(
        "arithmetic and precedence",
        "let x = 2 + 3 * 4; print(x);",
        ["14"],
    )

    check(
        "variables and assignment",
        "let x = 10; x = x + 5; print(x);",
        ["15"],
    )

    check(
        "if true branch",
        "let x = 12; if (x >= 10) { print(x); } else { print(0); }",
        ["12"],
    )

    check(
        "if false / else branch",
        "let x = 4; if (x >= 10) { print(x); } else { print(0); }",
        ["0"],
    )

    check(
        "while loop",
        "let x = 1; while (x <= 3) { print(x); x = x + 1; }",
        ["1", "2", "3"],
    )

    try:
        run_source("print(unknown);")
        raise AssertionError("undefined variable did not fail")
    except UndefinedVariableError:
        print("PASS: undefined variable error")

    try:
        run_source("print(10 / 0);")
        raise AssertionError("division by zero did not fail")
    except DivisionByZeroError:
        print("PASS: division by zero error")

    try:
        run_source("if (10) { print(1); }")
        raise AssertionError("invalid condition did not fail")
    except InvalidOperationError:
        print("PASS: invalid operation error")




def load_tests(loader, tests, pattern):
    """Keep earlier function-style checks in the standard-library suite."""
    import unittest

    return unittest.TestSuite(
        unittest.FunctionTestCase(check)
        for name, check in sorted(globals().items())
        if name.startswith("test_") and callable(check)
    )

if __name__ == "__main__":
    test_all()
    print("\nAll Part 4 interpreter tests passed!")
