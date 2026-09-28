# NovaLang

NovaLang is our group programming language project for CS 609. We have been developing this project step by step throughout the semester. In the previous parts, we worked on the language design, lexer, parser, and AST. In Part 4, we added an interpreter so that programs written in NovaLang can actually be executed.

## Project Progress

- Part 1: Language design and grammar
- Part 2: Lexer
- Part 3: Parser and AST
- Part 4: Interpreter and environment/symbol table

## Part 4

For Part 4, we added the interpreter and environment to our previous project. The interpreter reads the AST created by the parser and executes the program.

The following features are supported:

- Variable declaration
- Variable assignment
- Addition, subtraction, multiplication, and division
- Modulo operation
- Operator precedence
- Parentheses
- Comparison operators
- Boolean values
- Logical operators
- If/else statements
- While loops
- Print statements
- Runtime error handling

The comparison operators supported are:

`==`, `!=`, `<`, `>`, `<=`, `>=`

The logical operators supported are:

`&&`, `||`, `!`

Functions were included in our original language design, but functions are not required or implemented for Part 4.

## Project Files

The main files used in the project are:

lexer.py
parser.py
ast_nodes.py
environment.py
interpreter.py
grammar.ebnf
README.md
AI_USE_STATEMENT.md