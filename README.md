# NovaLang

NovaLang is a small programming language developed for the CS 609 final project. This repository follows one cumulative implementation: source code is tokenized, then later milestones will add parsing, an AST, and interpretation.

Repository: [krsnathkr/NovaLang](https://github.com/krsnathkr/NovaLang) (private).

## Current status

Part 1 defined the [language and EBNF grammar](<NovaLang - Final Project - Part 1 Language Design & Grammer.md>). Part 2 implements the lexer in `lexer.py`, with token definitions in that file, six test programs under `tests/programs/`, their token output under `tests/outputs/`, and automated checks in `tests/test_lexer.py`. The [Part 2 AI use statement](AI_USE_STATEMENT.md) records AI assistance. Parser, AST, interpreter, functions, scope, and the Boolean extension are planned for later parts; they are not implemented yet.

## Run the lexer

Python 3.9 or newer is required; there are no third-party dependencies.

```bash
python3 lexer.py tests/programs/declaration.nova
python3 -m unittest discover -s tests -v
```

The lexer prints one token per line. To see a source-located lexical error, run `python3 lexer.py tests/programs/invalid.nova` (expected exit status: 1). NovaLang uses `fn` for function definitions, as specified in Part 1.

## Part 2 contribution statement

The group reports equal contributions to this milestone, rounded to 33% each:

- Krishna Thakar — 33%
- Sarada Garlapati — 33%
- Rabin KC — 33%

These percentages are the group's statement, not a claim that each member already has a GitHub commit in this repository.
