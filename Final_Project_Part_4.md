# Final Project – Part 4: Interpreter & Control Structures

- **Due:** Sep 27 by 11:59pm
- **Points:** 100
- **Weight within Final Project:** 20%
- **Submission:** ZIP file containing the working interpreter

---

## Objective

Your language should now become executable.
Implement an interpreter that traverses the AST and executes programs written in your language.

---

## Required Features

Update the grammar, lexer, parser, and AST as needed to support every construct below.

### 1. Variable Assignment

```text
let x = 10;
let y = x + 5;
```

### 2. Arithmetic

Support:

- `+`
- `-`
- `*`
- `/`

Apply correct operator precedence.

### 3. Print

```text
print(x);
```

### 4. Comparisons

Support:

- `==`
- `!=`
- `<`
- `>`
- `<=`
- `>=`

Document how comparison results are represented and how conditions interpret them.

### 5. If/Else

**Example:**

```text
if (x >= 10) {
    print(x);
} else {
    print(0);
}
```

### 6. While Loops

**Example:**

```text
let x = 1;
while (x <= 5) {
    print(x);
    x = x + 1;
}
```

---

## Environment / Symbol Table

- Your interpreter must maintain variables using an appropriate environment or symbol table.
- Your group should be able to explain how values are stored and retrieved.

---

## Runtime Errors

At minimum, appropriately handle:

- Undefined variables
- Division by zero
- Unsupported operand or operator combinations

---

## Testing

Submit at least **five complete programs** that collectively demonstrate every required feature, with expected and actual output. Also include intentional runtime-error cases for undefined variables and division by zero.

---

## AI Use

Identify any AI assistance used during implementation. Also identify at least one AI-generated suggestion that your group verified, modified, corrected, or rejected.

---

## Submission Checklist

- Complete source code developed so far, including the updated lexer, parser, and AST.
- Interpreter.
- Environment/symbol table.
- Five or more test programs.
- Expected and actual output.
- Updated grammar.
- `README.md`.
- AI Use Statement.

---

## Grading Criteria (100 Points Total)

| Criterion | Points |
| :--- | :---: |
| Expressions & Variables | 20 |
| if/else | 15 |
| while | 15 |
| Environment/Symbol Table | 15 |
| Runtime Error Handling | 10 |
| Testing | 10 |
| Code Quality | 5 |
| AI Use Documentation | 5 |
| GitHub Development & Individual Contribution | 5 |
