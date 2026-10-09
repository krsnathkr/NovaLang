# Final Project – Part 3: Parser & Abstract Syntax Tree

- **Due:** Sep 20 by 11:59pm
- **Points:** 100
- **Weight within Final Project:** 15%
- **Submission:** ZIP file upload

---

## Objective

Develop a parser that converts the tokens produced by your lexer into an **Abstract Syntax Tree (AST)**.

For example, given:

```text
2 + 3 * 4
```

the AST should preserve operator precedence, for example:

```text
BinaryOp(+, Number(2), BinaryOp(*, Number(3), Number(4)))
```

---

## Requirements

Your parser should process:
- Numbers
- Variables
- Arithmetic expressions
- Parenthesized expressions
- Variable declarations and reassignment
- Print statements
- Multiple statements

At minimum, your AST should contain appropriate node types such as:
- `ProgramNode`
- `NumberNode`
- `VariableNode`
- `BinaryOpNode`
- `AssignmentNode`
- `PrintNode`

*(Note: You may use a different design if appropriate.)*

Later parts will extend the parser and AST with comparisons, blocks, control structures, functions, and the selected extension.

---

## Syntax Error Handling

Invalid syntax must produce a meaningful error message.

**Example:**

```text
let x = ;
```
should be identified as invalid syntax.

---

## Testing

1. Create at least **five** automated parser tests.
2. Demonstrate the generated AST for at least **three** different programs or expressions. These may be included among the five tests.

---

## AI Use

Identify any AI assistance used during implementation. Also identify at least **one** AI-generated suggestion that your group verified, modified, corrected, or rejected.

---

## Submission Checklist

Your submission ZIP file must contain:
1. Updated lexer.
2. Parser source code.
3. AST node implementation.
4. Updated BNF/EBNF grammar.
5. Five or more parser tests.
6. AST output for at least three examples.
7. `README.md` with instructions.
8. AI Use Statement.

---

## Grading Criteria (100 Points Total)

| Criterion | Points |
| :--- | :---: |
| **Parser Implementation** | 30 |
| **AST Design** | 20 |
| **Operator Precedence** | 10 |
| **Syntax Error Handling** | 10 |
| **Testing** | 15 |
| **Code Quality / Documentation** | 5 |
| **AI Use Documentation** | 5 |
| **GitHub Development & Individual Contribution** | 5 |
