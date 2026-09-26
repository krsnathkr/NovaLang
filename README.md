# NovaLang

NovaLang is the group's cumulative CS 609 programming language project. Work progresses through the six assignment parts in one implementation.

## Project progress

- **Part 1:** Language design and EBNF grammar in [NovaLang - Final Project - Part 1 Language Design & Grammer.md](<NovaLang - Final Project - Part 1 Language Design & Grammer.md>).
- **Part 2:** Lexer in `lexer.py`, with token examples and lexer checks under `tests/`.
- **Part 3:** Recursive-descent parser and AST in `parser.py` and `ast_nodes.py`.

The current parser covers numbers, variables, declarations, assignments, print statements, arithmetic, unary minus, parentheses, and operator precedence. Comparisons, control structures, functions, and the selected extension are reserved for later parts.

## Run the Part 3 parser examples

From the repository root:

```bash
python3 tests/test_parser.py
python3 tests/test_errors.py
python3 generate_ast_outputs.py
```

The parser examples are in `tests/programs/ast_example_*.nova`; their saved ASTs are in `tests/outputs/ast_example_*.txt`. The Part 2 lexer checks remain in `tests/test_lexer.py`.

## Part 2 contribution statement

The group reports equal contributions to Part 2, rounded to 33% each:

- Krishna Thakar — 33%
- Sarada Garlapati — 33%
- Rabin KC — 33%

These percentages are the group's statement, not a claim that each member already has a GitHub commit in this repository.
