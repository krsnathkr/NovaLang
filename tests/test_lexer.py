"""Part 2 lexer checks against the NovaLang Part 1 grammar."""

from pathlib import Path
import unittest

from lexer import LexicalError, tokenize


HERE = Path(__file__).resolve().parent


class LexerTests(unittest.TestCase):
    def check_example(self, name):
        source = (HERE / "programs" / f"{name}.nova").read_text(encoding="utf-8")
        expected = (HERE / "outputs" / f"{name}.txt").read_text(
            encoding="utf-8"
        ).splitlines()
        tokens = tokenize(source)
        self.assertEqual([str(token) for token in tokens], expected)
        return tokens

    def test_variable_declaration(self):
        tokens = self.check_example("declaration")
        self.assertEqual([token.type for token in tokens], [
            "LET", "ID", "ASSIGN", "NUMBER", "SEMICOLON"
        ])
        self.assertEqual((tokens[1].lexeme, tokens[1].line, tokens[1].column),
                         ("_price2", 1, 5))
        self.assertEqual(tokens[3].lexeme, "25.5")
        self.assertEqual(tokenize("letdown_2")[0].type, "ID")

    def test_arithmetic_expression(self):
        tokens = self.check_example("arithmetic")
        self.assertEqual([token.type for token in tokens[3:]], [
            "MINUS", "NUMBER", "PLUS", "LPAREN", "NUMBER", "STAR",
            "NUMBER", "RPAREN", "SLASH", "NUMBER", "PERCENT", "NUMBER",
            "SEMICOLON"
        ])
        self.assertEqual(tokens[4].lexeme, "2")  # Unary minus is its own token.

    def test_print_statement(self):
        tokens = self.check_example("print")
        self.assertEqual([token.type for token in tokens], [
            "PRINT", "LPAREN", "ID", "RPAREN", "SEMICOLON"
        ])

    def test_control_structures_comparisons_and_booleans(self):
        tokens = self.check_example("control")
        types = [token.type for token in tokens]
        for token_type in (
            "IF", "ELSE", "WHILE", "TRUE", "FALSE", "GREATER_EQUAL",
            "LESS_EQUAL", "LESS", "GREATER", "EQUAL_EQUAL", "BANG_EQUAL",
            "AND_AND", "OR_OR", "BANG", "LBRACE", "RBRACE"
        ):
            with self.subTest(token_type=token_type):
                self.assertIn(token_type, types)
        print_token = next(token for token in tokens if token.type == "PRINT")
        self.assertEqual((print_token.line, print_token.column), (2, 5))
        else_token = next(token for token in tokens if token.type == "ELSE")
        self.assertEqual((else_token.line, else_token.column), (3, 3))

    def test_function_definition_and_call(self):
        tokens = self.check_example("functions")
        types = [token.type for token in tokens]
        self.assertEqual(types[0], "FN")  # Part 1 uses fn, not function.
        self.assertIn("RETURN", types)
        self.assertEqual(types.count("COMMA"), 2)
        self.assertEqual([token.lexeme for token in tokens if token.type == "ID"],
                         ["add", "a", "b", "a", "b", "total", "add"])

    def test_invalid_input(self):
        source = (HERE / "programs" / "invalid.nova").read_text(encoding="utf-8")
        with self.assertRaises(LexicalError) as caught:
            tokenize(source)
        error = caught.exception
        self.assertEqual((error.line, error.column), (1, 12))
        self.assertIn("'@'", str(error))
        self.assertEqual(str(error), (HERE / "outputs" / "invalid.txt").read_text(
            encoding="utf-8"
        ).strip())

        for source, column in (
            ("a & b;", 3), ("a | b;", 3), ("12.", 1),
            ("1value", 1), (".5", 1), ("é", 1)
        ):
            with self.subTest(source=source):
                with self.assertRaises(LexicalError) as caught:
                    tokenize(source)
                self.assertEqual((caught.exception.line, caught.exception.column),
                                 (1, column))


if __name__ == "__main__":
    unittest.main()
