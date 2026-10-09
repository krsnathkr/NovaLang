# Repository Guidelines

## Project Structure & Module Organization

The six `Final_Project_Part_*.md` files are the cumulative assignment specifications. Read earlier parts before changing later work because the language design, grammar, lexer, parser, AST, and interpreter must remain compatible.

The implementation has not been added yet. Follow the Part 6 target layout when it is introduced: keep `lexer.py`, `parser.py`, `ast_nodes.py`, `interpreter.py`, `environment.py`, and `main.py` at the repository root; place automated tests and sample programs under `tests/`; document usage in `README.md`. Avoid separate implementations for each project part.

## Build, Test, and Development Commands

There is currently no build step or dependency manifest. Prefer the Python standard library unless a requirement justifies a dependency. Once the interpreter exists, keep these commands working and document any arguments in `README.md`:

```bash
python3 main.py <program-file>              # Run a source program
python3 -m unittest discover -s tests       # Run the complete test suite
python3 -m compileall -q .                  # Check Python syntax
```

## Coding Style & Naming Conventions

Use four-space indentation and PEP 8 naming: `snake_case` for functions and variables, `PascalCase` for AST node classes, and `UPPER_CASE` for token constants. Keep token names, grammar productions, AST nodes, and interpreter behavior synchronized. Use meaningful errors that include source location when available.

## Testing Guidelines

Use standard-library `unittest`; name files `test_*.py` and methods `test_<behavior>`. Add focused tests for valid programs plus lexical, syntax, and runtime failures. Every language feature should have expected-output coverage, including precedence, scope, and the chosen extension.

## Commit & Pull Request Guidelines

No Git history is available in this directory, so no existing convention can be inferred. Use short imperative commits such as `Add comparison parsing`. Pull requests should summarize language changes, identify affected pipeline stages, list tests run, and note grammar or documentation updates. Link the relevant assignment or issue when available.

## Agent-Specific Instructions

Preserve the six-part progression. Inspect related specifications before editing, avoid speculative scaffolding, and do not delete or rename files without explicit approval.


# Final Project Overview & Six-Week Roadmap
CS 609 Final Project: Design and Build a Mini Programming Language Interpreter
Over six weeks, your group will design a small programming language and implement an interpreter for it using Python.

The purpose of this project is to apply concepts from CS 609 in a practical setting. By completing the project, you will gain experience with language design, grammars, lexical analysis, parsing, abstract syntax trees, interpretation, scope, functions, and programming language implementation.

Your interpreter will follow the general processing pipeline:

Source Program → Lexer → Tokens → Parser → AST → Interpreter → Output

Six-Week Roadmap
Week	Project Part	Main Goal
1	Part 1	Language Design & BNF/EBNF Grammar
2	Part 2	Lexical Analyzer (Lexer)
3	Part 3	Parser & Abstract Syntax Tree
4	Part 4	Interpreter & Control Structures
5	Part 5	Functions, Scope & Extension Feature
6	Part 6	Integration, Testing, Report & Recorded Demonstration
Each part builds upon the previous part. You should therefore maintain and improve the same project throughout all six weeks.

Do not treat the assignments as six independent programming assignments.

Your GitHub repository should also demonstrate continuous development throughout the six-week project.