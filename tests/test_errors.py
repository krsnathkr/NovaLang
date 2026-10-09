"""Part 3 syntax-error regressions with assertions, not print-only checks."""

import unittest

from lexer import tokenize
from parser import Parser, ParseError


class ParserErrorTests(unittest.TestCase):
    def test_invalid_statements(self):
        for source in (
            "let x = ;", "let = 10;", "x = ;", "print();",
            "print(10;", "let x = 10",
        ):
            with self.subTest(source=source):
                with self.assertRaises(ParseError):
                    Parser(tokenize(source)).parse_program()


if __name__ == "__main__":
    unittest.main()
