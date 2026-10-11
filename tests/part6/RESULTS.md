# Part 6 verification results

No third-party packages are required. The October 11 cumulative audit reported:

- Python 3.11.14: `python3 -m unittest discover -s tests -v` — **67 tests passed**.
- Python 3.9.6: the same suite — **66 passed, 1 skipped**. The skipped check depends on Python's integer string digit-limit setting, which is unavailable on that host version.
- Python 3.13: all **42 Part 6 tests passed**.
- **12 complete valid programs**: exact API return values, console output, and CLI stdout matched independent expected files; exit 0 and empty stderr.
- **13 intentional failure programs**: CLI stderr exactly matched expected diagnostics; exit 1, empty stdout, no Python traceback.
- Token/AST inspection and legacy interpreter entry point passed their regression checks.
- All Python source files compile. Fresh CLI runs matched and refreshed all 25 Part 6 and 8 Part 4 expected/actual output pairs.

The saved [unittest.log](unittest.log) records the full Python 3.11.14 run.

The earlier October 8 record reported 64 cumulative tests. The suite has since grown; the counts above are the current audit results. The implementation audit also checked numeric edge cases: decimal arithmetic uses floating-point values; non-finite floating-point results are rejected with a NovaLang runtime error. Division returns a float, so a whole-number quotient can print as `2.0`. Very large integer input or output can encounter Python's configured decimal digit-conversion limit, so that specific check is version-dependent.

The Part 1 syntax and logical extension remain represented in the cumulative grammar and execute in the original sample programs. The first sample's division result is displayed as `2.0`, while its historical expected text says `2`; this follows the interpreter's floating-point division behavior.

## Coding requirement coverage

The following checklist maps the coding requirements to cumulative project artifacts. It records repository evidence, not a grade prediction.

| Canvas part | Coding evidence | Source |
| --- | --- | --- |
| Part 1 | The cumulative grammar and token specification define the language recognized by the lexer and parser. | [Canvas Part 1](https://canvas.semo.edu/courses/48106/assignments/816773) |
| Part 2 | Five lexer programs have saved token outputs and automated checks; `TOKEN_DEFINITIONS.md` documents token kinds and lexemes. | [Canvas Part 2](https://canvas.semo.edu/courses/48106/assignments/816775) |
| Part 3 | Eight parser cases and three saved AST outputs cover expressions and statement parsing. | [Canvas Part 3](https://canvas.semo.edu/courses/48106/assignments/816777) |
| Part 4 | Eight interpreter programs have expected and actual output files. | [Canvas Part 4](https://canvas.semo.edu/courses/48106/assignments/816778) |
| Part 5 | Six new programs and output files cover function definitions/calls, parameters, returns, scope, and recursion. | [Canvas Part 5](https://canvas.semo.edu/courses/48106/assignments/816801) |
| Part 6 | Twelve valid programs and thirteen error programs have expected/actual output; cumulative suite results are listed above. | [Canvas Part 6](https://canvas.semo.edu/courses/48106/assignments/816804) |

Part 2's five token-output cases are declaration, arithmetic, print, control structures, and functions. Parser cases and AST samples are in `tests/test_parser.py` and `tests/outputs/ast_example_1.txt` through `ast_example_3.txt`. Part 4 and 5 program pairs are under `tests/part4/` and `tests/part5/`.

Each program has `<name>.expected.txt` and `<name>.actual.txt` under `outputs/`. Actual files capture stdout for valid programs and stderr for error programs. Re-run a single fixture with `python3 main.py tests/part6/programs/01_arithmetic.nova` or `python3 main.py tests/part6/errors/error01_lexical.nova`.

| Program | Exit status | Expected vs. actual |
| --- | --- | --- |
| [01_arithmetic.nova](programs/01_arithmetic.nova) | 0 | PASS |
| [02_precedence.nova](programs/02_precedence.nova) | 0 | PASS |
| [03_variables.nova](programs/03_variables.nova) | 0 | PASS |
| [04_print_values.nova](programs/04_print_values.nova) | 0 | PASS |
| [05_comparisons.nova](programs/05_comparisons.nova) | 0 | PASS |
| [06_if_else.nova](programs/06_if_else.nova) | 0 | PASS |
| [07_while_sum.nova](programs/07_while_sum.nova) | 0 | PASS |
| [08_functions.nova](programs/08_functions.nova) | 0 | PASS |
| [09_scope.nova](programs/09_scope.nova) | 0 | PASS |
| [10_recursion.nova](programs/10_recursion.nova) | 0 | PASS |
| [11_logical_short_circuit.nova](programs/11_logical_short_circuit.nova) | 0 | PASS |
| [12_integrated.nova](programs/12_integrated.nova) | 0 | PASS |
| [error01_lexical.nova](errors/error01_lexical.nova) | 1 | PASS |
| [error02_syntax.nova](errors/error02_syntax.nova) | 1 | PASS |
| [error03_undefined_variable.nova](errors/error03_undefined_variable.nova) | 1 | PASS |
| [error04_division_zero.nova](errors/error04_division_zero.nova) | 1 | PASS |
| [error05_modulo_zero.nova](errors/error05_modulo_zero.nova) | 1 | PASS |
| [error06_invalid_operand.nova](errors/error06_invalid_operand.nova) | 1 | PASS |
| [error07_invalid_condition.nova](errors/error07_invalid_condition.nova) | 1 | PASS |
| [error08_undefined_function.nova](errors/error08_undefined_function.nova) | 1 | PASS |
| [error09_argument_count.nova](errors/error09_argument_count.nova) | 1 | PASS |
| [error10_return_outside_function.nova](errors/error10_return_outside_function.nova) | 1 | PASS |
| [error11_duplicate_parameter.nova](errors/error11_duplicate_parameter.nova) | 1 | PASS |
| [error12_local_scope.nova](errors/error12_local_scope.nova) | 1 | PASS |
| [error13_recursion_limit.nova](errors/error13_recursion_limit.nova) | 1 | PASS |

## Feature coverage

| Required feature | Valid program |
| --- | --- |
| Arithmetic including division/modulo/decimals | 01_arithmetic |
| Precedence, parentheses, associativity | 02_precedence |
| Declarations and reassignment | 03_variables |
| Numeric and Boolean print output | 04_print_values |
| All six comparison operators | 05_comparisons |
| Both if/else branches and nested control flow | 06_if_else |
| While iterations, outer assignment, zero iterations | 07_while_sum |
| Functions, parameters, nested calls, zero arguments | 08_functions |
| Global/local/block scope, shadowing, fresh call locals | 09_scope |
| Selected extension: recursion | 10_recursion |
| Boolean/logical operators and short circuit | 11_logical_short_circuit |
| Functions, recursion, loops, scopes, logic together | 12_integrated |

## Corrections verified during integration

The original default discovery failed on Python 3.9 because `BlockNode | None` was evaluated at import. Postponed annotations corrected it. Discovery also omitted the earlier function-style checks and subdirectories; unittest adapters and package markers now execute them. Earlier `fn` syntax and general expression statements were restored alongside the Part 5 `function` spelling. Duplicate parameters now produce a located syntax error. Both entry points report lexical, syntax, runtime, file, and recursion-limit failures cleanly.

Lexer/parser diagnostics include line and column when a token is available. EOF syntax diagnostics use the nearest preceding token. Runtime diagnostics identify the failing operation or name; the current AST does not retain source positions.
