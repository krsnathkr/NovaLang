import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from lexer import tokenize
from parser import Parser


def parse(source):
    tokens = tokenize(source)
    parser = Parser(tokens)
    return parser.parse_program()


def test_number_expression():
    tokens = tokenize("42")
    parser = Parser(tokens)

    ast = parser.parse_expression()

    output = ast.pretty()

    assert output == "NumberNode(42)"

    print("PASS: Number expression")


def test_operator_precedence():
    tokens = tokenize("2 + 3 * 4")
    parser = Parser(tokens)

    ast = parser.parse_expression()

    output = ast.pretty()

    expected = """BinaryOpNode(+)
  NumberNode(2)
  BinaryOpNode(*)
    NumberNode(3)
    NumberNode(4)"""

    assert output == expected

    print("PASS: Operator precedence")


def test_variable_declaration():
    ast = parse("let x = 10;")

    output = ast.pretty()

    expected = """ProgramNode
  AssignmentNode(Declaration)
    VariableNode(x)
    NumberNode(10)"""

    assert output == expected

    print("PASS: Variable declaration")


def test_assignment():
    ast = parse("x = 20;")

    output = ast.pretty()

    expected = """ProgramNode
  AssignmentNode(Assignment)
    VariableNode(x)
    NumberNode(20)"""

    assert output == expected

    print("PASS: Assignment")


def test_print_statement():
    ast = parse("print(x + 5);")

    output = ast.pretty()

    expected = """ProgramNode
  PrintNode
    BinaryOpNode(+)
      VariableNode(x)
      NumberNode(5)"""

    assert output == expected

    print("PASS: Print statement")


def test_multiple_statements():
    ast = parse("""
        let x = 10;
        x = x + 5;
        print(x);
    """)

    output = ast.pretty()

    expected = """ProgramNode
  AssignmentNode(Declaration)
    VariableNode(x)
    NumberNode(10)
  AssignmentNode(Assignment)
    VariableNode(x)
    BinaryOpNode(+)
      VariableNode(x)
      NumberNode(5)
  PrintNode
    VariableNode(x)"""

    assert output == expected

    print("PASS: Multiple statements")


def test_parentheses():
    tokens = tokenize("(2 + 3) * 4")
    parser = Parser(tokens)

    ast = parser.parse_expression()

    output = ast.pretty()

    expected = """BinaryOpNode(*)
  BinaryOpNode(+)
    NumberNode(2)
    NumberNode(3)
  NumberNode(4)"""

    assert output == expected

    print("PASS: Parentheses")


def test_unary_minus():
    tokens = tokenize("-5")
    parser = Parser(tokens)

    ast = parser.parse_expression()

    output = ast.pretty()

    expected = """UnaryOpNode(-)
  NumberNode(5)"""

    assert output == expected

    print("PASS: Unary minus")

if __name__ == "__main__":
    test_number_expression()
    test_operator_precedence()
    test_variable_declaration()
    test_assignment()
    test_print_statement()
    test_multiple_statements()
    test_parentheses()
    test_unary_minus()

    print("\nAll parser tests passed!")