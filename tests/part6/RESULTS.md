# Part 6 verification results

Verified using Python 3.9.6 on macOS. No third-party packages are required.

- `python3 -m unittest discover -s tests -v`: **64 tests passed**, including cumulative Parts 2–5 checks and the final integration suite. Detailed output: [unittest.log](unittest.log).
- `python3 -m compileall -q .`: **exit 0**, no syntax errors.
- **12 complete valid programs**: exact API return values, console output, and CLI stdout matched independent expected files; exit 0 and empty stderr.
- **13 intentional failure programs**: CLI stderr exactly matched expected diagnostics; exit 1, empty stdout, no Python traceback.
- Token/AST inspection and legacy interpreter entry point passed their regression checks.

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
