# Final Project – Part 5: Functions, Scope & Extension Feature

- **Due:** Oct 4 by 11:59pm
- **Points:** 100
- **Weight within Final Project:** 20%
- **Submission:** ZIP file upload

---

## Objective

Extend your interpreter to support functions, variable scope, and one additional programming-language feature.

---

## Functions

Your language must support simple functions.

### Example

```text
function add(a, b) {
  return a + b;
}

let result = add(10, 20);
print(result);
```

### Requirements

Your implementation must support:

- Function definitions
- Parameters
- Function calls
- Return values
- Local variables

Each call must create a fresh local environment, bind arguments to parameters, and return control and a value to the caller. Report meaningful errors for undefined functions and incorrect argument counts.

---

## Scope

Your interpreter must distinguish between global and local scope.

### Example

```text
let x = 10;

function test() {
  let x = 20;
  print(x);
}

test();
print(x);
```

**Expected Output:**

```text
20
10
```

> **Note:** Your group must be able to explain how scope is represented in the interpreter.

Local variables may shadow global variables. Name lookup should check the current local environment before the global environment.

---

## Extension Feature

Implement at least one additional feature.

### Possible Options

- `for` loops
- Arrays/lists
- Strings
- User input
- `break` and `continue`
- Recursion
- Built-in mathematical functions
- Constants
- Comments
- Additional data types

*You may propose another feature with instructor approval.*

Update the grammar, lexer, parser, AST, interpreter, tests, and documentation wherever the extension requires changes.

---

## Testing

Create at least **five new test programs** that collectively demonstrate definitions, calls, parameters, returns, global and local scope, shadowing, and the extension. Include expected and actual output.

---

## AI Use

Identify any AI assistance used during implementation. Also identify at least one AI-generated suggestion that your group verified, modified, corrected, or rejected.

---

## Submission Checklist

Submit a ZIP file containing:

- Complete updated interpreter implementing functions, scope, and the extension.
- Updated AST components.
- Updated BNF/EBNF.
- Five or more new tests.
- Expected and actual output.
- `README.md`.
- AI Use Statement.

---

## Grading Criteria (100 Points Total)

| Criterion | Points |
| :--- | :---: |
| Function Definitions & Calls | 20 |
| Parameters & Return Values | 15 |
| Scope | 20 |
| Extension Feature | 20 |
| Testing | 10 |
| Code Quality | 5 |
| AI Use Documentation | 5 |
| GitHub Development & Individual Contribution | 5 |
| **Total** | **100** |
