from pathlib import Path

from interpreter import run_source


BASE_DIR = Path(__file__).parent
PROGRAM_DIR = BASE_DIR / "programs"
OUTPUT_DIR = BASE_DIR / "outputs"


def run_test(program_name, output_name):
    source = (PROGRAM_DIR / program_name).read_text(encoding="utf-8")

    actual_output = run_source(source)

    expected_output = (
        OUTPUT_DIR / output_name
    ).read_text(encoding="utf-8").splitlines()

    assert actual_output == expected_output


def test_basic_function():
    run_test(
        "test1_basic_function.nova",
        "test1_basic_function.txt",
    )


def test_parameters():
    run_test(
        "test2_parameters.nova",
        "test2_parameters.txt",
    )


def test_scope():
    run_test(
        "test3_scope.nova",
        "test3_scope.txt",
    )


def test_function_scope():
    run_test(
        "test4_function_scope.nova",
        "test4_function_scope.txt",
    )


def test_recursion():
    run_test(
        "test5_recursion.nova",
        "test5_recursion.txt",
    )


def test_multiple_calls():
    run_test(
        "test6_multiple_calls.nova",
        "test6_multiple_calls.txt",
    )


def load_tests(loader, tests, pattern):
    """Keep earlier function-style checks in the standard-library suite."""
    import unittest

    return unittest.TestSuite(
        unittest.FunctionTestCase(check)
        for name, check in sorted(globals().items())
        if name.startswith("test_") and callable(check)
    )
