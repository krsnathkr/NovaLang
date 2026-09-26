# AI Use Statement

ChatGPT (OpenAI) was used as an AI-assisted development and learning
tool during the development of NovaLang Part 3.

ChatGPT was used for:

- Understanding parser and Abstract Syntax Tree (AST) concepts.
- Discussing parser architecture and implementation approaches.
- Understanding and implementing operator precedence.
- Troubleshooting programming errors and implementation issues.
- Designing parser test cases and syntax-error test cases.
- Reviewing and improving code structure and documentation.
- Understanding the requirements and organization of the Part 3 deliverables.

The NovaLang lexer, parser, AST implementation, tests, grammar, and
documentation were reviewed and tested by the project team.

AI-generated suggestions were evaluated and adapted to the existing
NovaLang lexer, project requirements, grammar, and AST design rather
than being accepted without verification.

All implemented functionality was tested locally using NovaLang
programs and parser test cases.

### Part 3 AI Use Statement

ChatGPT (OpenAI) assisted with learning parser and AST concepts, parser architecture, operator precedence, troubleshooting, test-case design, and documentation. The project team reports reviewing the lexer, parser, AST, tests, grammar, and documentation, and evaluating AI suggestions against the existing NovaLang grammar and project requirements.

One parser design suggestion the team verified was to parse multiplication, division, and modulo at a tighter precedence level than addition and subtraction. The Part 3 grammar and the saved AST for `2 + 3 * 4` demonstrate that behavior.

The team reports testing the Part 3 work with NovaLang programs and parser cases. Group members should review and rerun the checks before submission.
