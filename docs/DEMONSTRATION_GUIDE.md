# NovaLang Recorded Demonstration Guide

Target length: about 12 minutes. Before recording, open the project root in a terminal and make sure the final test command succeeds. Replace the contribution prompts with each person's own accurate account. Every listed group member must speak on camera or in the recording and explain a component they worked on; each should also show that they understand the full pipeline. Do not leave a person's segment to one presenter.

## Timed script

| Time | Presenter / screen | What to show and say |
| --- | --- | --- |
| 0:00-1:00 | Sarada, Krishna, and Rabin introduce themselves | Say: “We are the NovaLang group: Sarada Garlapati, Krishna Thakar, and Rabin KC. NovaLang is our small interpreted language for demonstrating a complete language pipeline. Our selected Part 5 extension is recursion.” Each person names their milestone work: Sarada Parts 1 and 3; Krishna Parts 2 and 6; Rabin Parts 4 and 5. |
| 1:00-2:00 | Terminal and project tree | Show `lexer.py`, `parser.py`, `ast_nodes.py`, `interpreter.py`, `environment.py`, `main.py`, and `tests/`. Explain source → tokens → AST → evaluation/output. Lexer recognizes source lexemes, parser checks grammar and builds structure, AST stores that structure, interpreter evaluates it, environment stores variables/functions. |
| 2:00-3:15 | Token inspection | Run `python3 main.py --tokens tests/programs/functions.nova`. Point out examples of identifiers, keywords, numbers, operators, delimiters, and their line/column locations. Note that whitespace is skipped and invalid characters raise a lexical error. |
| 3:15-4:45 | AST inspection | Run `python3 main.py --ast tests/part6/programs/02_precedence.nova`. Explain that `2 + 3 * 4` produces a tree with `+` at the top and `*` as its right operand, so multiplication occurs first and the result is 14. Show the node labels emitted by `--ast`. |
| 4:45-5:30 | Execute arithmetic and variables | Run `python3 main.py tests/part6/programs/01_arithmetic.nova`. Explain declarations, assignment, numeric operators, and print output. Compare the terminal output with `tests/part6/outputs/01_arithmetic.expected.txt`. |
| 5:30-6:30 | Comparisons and control flow | Run `python3 main.py tests/part4/programs/test2_comparisons_if_else.nova`, then `python3 main.py tests/part4/programs/test3_while.nova`. Explain Boolean comparison results, the chosen branch, and repeated condition evaluation in the loop. |
| 6:30-8:00 | Functions and scope | Run `python3 main.py tests/part5/programs/test3_scope.nova`, followed by `python3 main.py tests/part5/programs/test1_basic_function.nova`. Explain parameter binding, return values, and why a local `x` does not overwrite the global `x`. |
| 8:00-9:00 | Recursion extension | Run `python3 main.py tests/part5/programs/test5_recursion.nova`. Trace factorial's base case and recursive call for a couple of levels; explain that every call has a fresh local environment. |
| 9:00-10:00 | Errors | Show and run `tests/part6/errors/error01_lexical.nova`, `tests/part6/errors/error02_syntax.nova`, and `tests/part6/errors/error04_division_zero.nova`. Explain each message and source location where available. Errors are expected to exit as errors; continue recording after each. |
| 10:00-11:15 | Focused code walkthrough | Sarada explains one parser/AST portion; Krishna shows the lexer or Part 6 entry point; Rabin shows interpreter/environment and function calls. Across those segments, cover lexer, parser, AST, interpreter, and environment. Avoid scrolling through whole files. |
| 11:15-12:00 | Krishna leads tests and AI use; all members add understanding | Run `python3 -m unittest discover -s tests`. Briefly describe how AI tools were used, one correction made during integration (postponed annotation evaluation for Python 3.9 compatibility, and retaining the original `fn` spelling while adding `function` compatibility), and how the tests checked behavior. Each member should explain that they understand the integrated behavior. Only claim checks that were actually run and reviewed. |
| 12:00-12:30 | Close | Recap recursion as the extension and state that the report, project archive, GitHub link, and accessible recording are the submission items. The recording and Canvas upload remain to be completed by the group. |

## Before recording

- Run the documented tests and each demo command once; use the actual final filenames if integration changes them.
- Arrange a speaking segment for Sarada Garlapati, Krishna Thakar, and Rabin KC. Each person should state their Parts 1-6 contribution as listed in `docs/CONTRIBUTIONS.md`.
- Keep the terminal font readable. Show the command, source example, and output together where possible.
- Do not claim a recording, Canvas upload, latest GitHub push, or individual work that has not happened or been verified.
- If the group shares a link, test it in a private browser window before submission.
