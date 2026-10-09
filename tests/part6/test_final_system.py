"""Verify complete programs through both the API and the actual command line."""

import contextlib
import io
from pathlib import Path
import subprocess
import sys
import unittest

from environment import UndefinedVariableError
from interpreter import FunctionError, Interpreter, run_source
from lexer import tokenize
from parser import ParseError, Parser

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent


def cli(program_file, *options, entry="main.py"):
    return subprocess.run(
        [sys.executable, str(ROOT / entry), str(program_file), *options],
        capture_output=True, text=True, cwd=ROOT, check=False,
    )


class FinalProgramTests(unittest.TestCase):
    def check_success(self, name):
        source_path = HERE / "programs" / (name + ".nova")
        expected = (HERE / "outputs" / (name + ".expected.txt")).read_text()
        console = io.StringIO()
        with contextlib.redirect_stdout(console):
            output = run_source(source_path.read_text())
        self.assertEqual(output, expected.splitlines())
        self.assertEqual(console.getvalue(), expected)
        result = cli(source_path)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, expected)
        self.assertEqual(result.stderr, "")

    def check_error(self, name):
        result = cli(HERE / "errors" / (name + ".nova"))
        expected = (HERE / "outputs" / (name + ".expected.txt")).read_text()
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stderr, expected)
        self.assertEqual(result.stdout, "")
        self.assertNotIn("Traceback", result.stderr)

    def test_01_arithmetic(self):
        self.check_success("01_arithmetic")

    def test_02_precedence(self):
        self.check_success("02_precedence")

    def test_03_variables(self):
        self.check_success("03_variables")

    def test_04_print_values(self):
        self.check_success("04_print_values")

    def test_05_comparisons(self):
        self.check_success("05_comparisons")

    def test_06_if_else(self):
        self.check_success("06_if_else")

    def test_07_while_sum(self):
        self.check_success("07_while_sum")

    def test_08_functions(self):
        self.check_success("08_functions")

    def test_09_scope(self):
        self.check_success("09_scope")

    def test_10_recursion(self):
        self.check_success("10_recursion")

    def test_11_logical_short_circuit(self):
        self.check_success("11_logical_short_circuit")

    def test_12_integrated(self):
        self.check_success("12_integrated")

    def test_error01_lexical(self):
        self.check_error("error01_lexical")

    def test_error02_syntax(self):
        self.check_error("error02_syntax")

    def test_error03_undefined_variable(self):
        self.check_error("error03_undefined_variable")

    def test_error04_division_zero(self):
        self.check_error("error04_division_zero")

    def test_error05_modulo_zero(self):
        self.check_error("error05_modulo_zero")

    def test_error06_invalid_operand(self):
        self.check_error("error06_invalid_operand")

    def test_error07_invalid_condition(self):
        self.check_error("error07_invalid_condition")

    def test_error08_undefined_function(self):
        self.check_error("error08_undefined_function")

    def test_error09_argument_count(self):
        self.check_error("error09_argument_count")

    def test_error10_return_outside_function(self):
        self.check_error("error10_return_outside_function")

    def test_error11_duplicate_parameter(self):
        self.check_error("error11_duplicate_parameter")

    def test_error12_local_scope(self):
        self.check_error("error12_local_scope")

    def test_error13_recursion_limit(self):
        self.check_error("error13_recursion_limit")


class IntegrationRegressionTests(unittest.TestCase):
    def capture(self, source):
        with contextlib.redirect_stdout(io.StringIO()):
            return run_source(source)

    def test_both_function_spellings(self):
        for keyword in ("fn", "function"):
            with self.subTest(keyword=keyword):
                self.assertEqual(self.capture(
                    f"{keyword} twice(x) {{ return x * 2; }} print(twice(6));"
                ), ["12"])

    def test_expression_statements_from_original_grammar(self):
        self.assertEqual(self.capture("2 + 3; (4 * 5); true; !false; print(7);"), ["7"])

    def test_function_uses_lexical_scope(self):
        self.assertEqual(self.capture(
            "let x = 1; fn read() { return x; } "
            "fn caller() { let x = 99; return read(); } print(caller());"
        ), ["1"])

    def test_return_exits_nested_control_flow(self):
        self.assertEqual(self.capture(
            "fn find(n) { while (n > 0) { if (n == 3) { return n; } "
            "n = n - 1; } return 0; } print(find(5)); print(find(0));"
        ), ["3", "0"])

    def test_fresh_function_locals(self):
        self.assertEqual(self.capture(
            "fn next(n) { let x = n; x = x + 1; return x; } "
            "print(next(1)); print(next(8));"
        ), ["2", "9"])

    def test_block_locals_do_not_leak(self):
        with self.assertRaises(UndefinedVariableError):
            self.capture("if (true) { let hidden = 2; } print(hidden);")

    def test_runtime_failure_restores_environment_and_function_depth(self):
        machine = Interpreter()
        root_environment = machine.environment
        program = Parser(tokenize(
            "fn bad() { if (true) { print(missing); } } bad();"
        )).parse_program()
        with self.assertRaises(UndefinedVariableError):
            machine.execute(program)
        self.assertIs(machine.environment, root_environment)
        self.assertEqual(machine.function_depth, 0)
        with self.assertRaises(FunctionError):
            machine.execute(Parser(tokenize("return 1;")).parse_program())

    def test_end_of_input_syntax_error_has_nearest_location(self):
        for source in ("print(1)", "if (true) {", "let x ="):
            with self.subTest(source=source):
                with self.assertRaisesRegex(ParseError, "line 1, column"):
                    Parser(tokenize(source)).parse_program()

    def test_token_inspection_does_not_execute(self):
        result = cli(HERE / "errors" / "error03_undefined_variable.nova", "--tokens")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("ID(missing) @ 1:7", result.stdout)
        self.assertEqual(result.stderr, "")

    def test_ast_preserves_precedence(self):
        result = cli(HERE / "programs" / "02_precedence.nova", "--ast")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(
            "BinaryOpNode(+)\n      NumberNode(2)\n      BinaryOpNode(*)\n"
            "        NumberNode(3)\n        NumberNode(4)", result.stdout,
        )
        self.assertNotIn("\n14\n", result.stdout)

    def test_inspection_modes_are_mutually_exclusive(self):
        result = cli(HERE / "programs" / "01_arithmetic.nova", "--ast", "--tokens")
        self.assertEqual(result.returncode, 2)
        self.assertIn("not allowed", result.stderr)

    def test_missing_file_is_readable_error(self):
        result = cli(HERE / "file_that_does_not_exist.nova")
        self.assertEqual(result.returncode, 1)
        self.assertIn("File error:", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_legacy_interpreter_cli_handles_all_error_stages(self):
        for name in ("error01_lexical", "error02_syntax", "error04_division_zero"):
            with self.subTest(name=name):
                result = cli(HERE / "errors" / (name + ".nova"), entry="interpreter.py")
                expected = (HERE / "outputs" / (name + ".expected.txt")).read_text()
                self.assertEqual(result.returncode, 1)
                self.assertEqual(result.stderr, expected)

    def test_part4_expected_outputs_remain_compatible(self):
        for program in sorted((ROOT / "tests" / "part4" / "programs").glob("*.nova")):
            with self.subTest(program=program.name):
                expected = (program.parent.parent / "outputs" /
                            (program.stem + ".expected.txt")).read_text()
                result = cli(program)
                actual = result.stderr if result.returncode else result.stdout
                self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
