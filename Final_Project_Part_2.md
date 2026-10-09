# Final Project – Part 2: Lexical Analyzer (Lexer)

- **Due:** Sep 13 by 11:59pm
- **Points:** 100
- **Weight within Final Project:** 10%
- **Submission:** ZIP file containing source code, tests, and documentation

---

## Objective

Implement the lexer for the programming language designed in Part 1.
The lexer converts source code into a sequence of tokens.

*Example:*

```text
let x = 10 + 5;
```

*Might generate:*

```text
LET
ID(x)
ASSIGN
NUMBER(10)
PLUS
NUMBER(5)
SEMICOLON
```

---

## Requirements

Your lexer must recognize every keyword and symbol defined in Part 1, including:

- Keywords
- Identifiers
- Integer and decimal numbers
- Arithmetic operators
- Comparison operators
- Assignment operator
- Parentheses
- Braces
- Commas
- Semicolons
- Whitespace, which should be skipped unless your language makes it meaningful

The lexer must also recognize the keywords required for:

- `let`
- `print`
- `if`
- `else`
- `while`
- `function`
- `return`

*(or the equivalent keywords defined by your language)*

---

## Error Handling

Your lexer must detect invalid characters and report a meaningful error with the source location when available.

*Example:*

```text
let x = 10 @ 5;
```
This should produce a meaningful lexical error rather than an unexplained Python exception.

---

## Testing

Create at least **five** different lexer test cases. Your tests should include:
1. Variable declaration
2. Arithmetic expression
3. Print statement
4. Control structure
5. Invalid input

Together, the tests should cover all token categories, including multi-character comparison operators and function-related keywords.

---

## Required Submission Content

Your ZIP file must contain:
1. Lexer source code
2. Token definitions
3. Five or more test cases
4. Lexer output for each test
5. Updated grammar (if changes were made)
6. Brief `README.md` explaining how to run the lexer
7. AI Use Statement
8. GitHub repository link and contribution evidence

---

## AI Use

Identify any AI assistance used during implementation. Also identify at least **one** AI-generated suggestion that your group verified, modified, corrected, or rejected.

---

## Grading Criteria (100 Points Total)

| Criterion | Points |
| :--- | :---: |
| **Token Recognition** | 30 |
| **Correct Lexer Operation** | 20 |
| **Error Handling** | 15 |
| **Testing** | 15 |
| **Code Organization & Documentation** | 10 |
| **AI Use Documentation** | 5 |
| **GitHub Development & Individual Contribution** | 5 |
