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

The tests retain the cumulative Parts 2–5 checks and expected/actual output. Part 6 includes 12 valid programs and 13 separate lexical, syntax, and runtime failure examples. The October 11 audit results across Python versions, including numerical edge cases, are recorded in [`tests/part6/RESULTS.md`](tests/part6/RESULTS.md).

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

The result is `120`. Each call gets a fresh local environment whose parent is the function's defining environment. Local declarations can shadow outer variables. Conditions require Boolean values. Logical `&&` and `||` short-circuit. Arithmetic supports `+`, `-`, `*`, `/`, and `%`; comparisons return Booleans. Decimal values use floating-point arithmetic, and division returns a float: a whole-number quotient can print as `2.0`. Non-finite numeric results and values that exceed the host's decimal conversion limit produce readable NovaLang runtime errors; exact behavior for very large integer input/output can depend on the Python version's configured digit limit.

From highest to lowest, expression precedence is: parentheses; unary `!` and `-`; `*`, `/`, `%`; `+`, `-`; relational comparisons; equality; `&&`; `||`. Operators at the same binary level associate left to right. Thus `2 + 3 * 4` parses as addition whose right child is multiplication, and evaluates to `14`.

## Project map

- `lexer.py`, `parser.py`, `ast_nodes.py`: tokenization, recursive-descent parsing, and tree nodes.
- [`TOKEN_DEFINITIONS.md`](TOKEN_DEFINITIONS.md): token names and the lexemes or patterns that produce them.
- `interpreter.py`, `environment.py`: evaluation, function calls, errors, and variable storage.
- `main.py`: command-line entry point.
- `grammar.ebnf`: grammar used by the implementation.
- `tests/`: programs, automated tests, and output examples.

## Project record

The language and grammar began in Part 1, followed by the lexer (Part 2), parser and AST (Part 3), interpreter and control flow (Part 4), and functions, scope, and recursion (Part 5). The separately submitted final report describes the integrated Part 6 system. The integrated system is published in this repository, and the earlier milestones remain in its commit history.

The separately submitted report PDF includes the individual contribution statement and AI-use documentation. The local `docs/` folder is excluded from Git so the report and recording materials can be submitted separately.

Project repository: [github.com/krsnathkr/NovaLang](https://github.com/krsnathkr/NovaLang) (private). Final system: [main](https://github.com/krsnathkr/NovaLang/tree/main). Part 6 integration: [pull request #1](https://github.com/krsnathkr/NovaLang/pull/1).
