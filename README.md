# NovaLang

NovaLang is a small interpreted language developed cumulatively for CS 609. Its pipeline is source text, lexical tokens, an abstract syntax tree, and interpreter output. It supports numeric and Boolean values, variables, arithmetic, comparisons, logical operators, conditionals, loops, functions, lexical parent scopes, and recursion.

## Run a program

```sh
python3 main.py tests/part5/programs/test5_recursion.nova
```

Inspect the lexer or parser without executing the program:

```sh
python3 main.py --tokens tests/programs/functions.nova
python3 main.py --ast tests/part6/programs/02_precedence.nova
```

`--tokens` prints token type, value, and source position. `--ast` prints the parsed tree. These options are mutually exclusive. With no inspection option, the interpreter executes the source file. User-facing errors include lexical, parse, and runtime failures with source location where available.

## Test

NovaLang uses Python 3.9 or newer and only the Python standard library; there is no dependency installation step.

Run the complete standard-library test suite from the project root:

```sh
python3 -m unittest discover -s tests
```

Check Python syntax with:

```sh
python3 -m compileall -q .
```

The repository also includes the earlier Part 4 and Part 5 pytest commands and captured expected/actual output under `tests/`. Part 6 includes 12 valid programs covering arithmetic and precedence, variables, printing, comparisons, conditionals, loops, functions, scope, recursion, logical short-circuiting, and an integrated example. Thirteen separate examples exercise lexical, syntax, and runtime failures. On Python 3.9.6, the implementation agent reported 64 passing tests and exact expected/actual matches for all 25 Part 6 fixtures. See [`tests/part6/RESULTS.md`](tests/part6/RESULTS.md); the group should review the evidence before submission.

## Language notes

Statements end in semicolons; blocks use braces. Variables are declared with `let`. Functions use the original `fn` spelling. The lexer also accepts `function` for compatibility with later examples:

```text
fn factorial(n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

print(factorial(5));
```

The result is `120`. Each call gets a fresh local environment whose parent is the function's defining environment. Local declarations can shadow outer variables. Conditions require Boolean values. Logical `&&` and `||` short-circuit. Arithmetic supports `+`, `-`, `*`, `/`, and `%`; comparisons return Booleans.

From highest to lowest, expression precedence is: parentheses; unary `!` and `-`; `*`, `/`, `%`; `+`, `-`; relational comparisons; equality; `&&`; `||`. Operators at the same binary level associate left to right. Thus `2 + 3 * 4` parses as addition whose right child is multiplication, and evaluates to `14`.

## Project map

- `lexer.py`, `parser.py`, `ast_nodes.py`: tokenization, recursive-descent parsing, and tree nodes.
- `interpreter.py`, `environment.py`: evaluation, function calls, errors, and variable storage.
- `main.py`: command-line entry point.
- `grammar.ebnf`: grammar used by the implementation.
- `tests/`: programs, automated tests, and output examples.
- `docs/`: final report, demonstration guide, contribution statement, and submission checklist.

## Project record

The language and grammar began in Part 1, followed by the lexer (Part 2), parser and AST (Part 3), interpreter and control flow (Part 4), and functions, scope, and recursion (Part 5). The final report and demonstration guide describe the integrated Part 6 system. Confirm that the latest local changes are committed and pushed before submitting the GitHub link.

See [`AI_USE_STATEMENT.md`](AI_USE_STATEMENT.md) for the cumulative account of AI assistance and [`docs/FINAL_REPORT.pdf`](docs/FINAL_REPORT.pdf) for the written report.

Project repository: [github.com/krsnathkr/NovaLang](https://github.com/krsnathkr/NovaLang) (private). The link identifies the existing repository; confirm the final Part 6 changes are pushed and visible on the submitted branch before turning it in.
