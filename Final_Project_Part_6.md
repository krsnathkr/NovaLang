# Final Project – Part 6: Final System, Report & Recorded Demonstration

- **Due:** Oct 11 by 11:59pm
- **Points:** 100
- **Weight within Final Project:** 25%
- **Submission:** Complete project ZIP, project report, recorded demonstration, and supporting items in the final checklist

---

## Objective

Complete, integrate, test, document, and demonstrate your programming language and interpreter.

Your final system should demonstrate the complete programming language processing pipeline:

```text
Source Program → Lexer → Tokens → Parser → AST → Interpreter → Output
```

---

## Final Required Features

Your completed interpreter must support:

- Variable declarations and assignments
- Arithmetic expressions
- Correct operator precedence
- Comparison operators
- Print statements
- `if`/`else` statements
- `while` loops
- Functions
- Parameters and return values
- Global and local scope
- Your selected extension feature
- Lexical error handling
- Syntax error handling
- Basic runtime error handling

---

## Final Test Suite

Create at least 10 complete, valid test programs demonstrating:

1. Arithmetic operations
2. Operator precedence
3. Variables and assignments
4. Print statements
5. Comparisons
6. `if`/`else`
7. `while` loops
8. Functions
9. Variable scope
10. Your extension feature

Also include intentional-error tests for lexical, syntax, and runtime failures. These are separate from the 10 valid programs.

---

## Project Report

Submit a **4–6 page report** explaining:

- Your programming language and its purpose
- Language design decisions
- BNF/EBNF grammar
- Lexer design
- Parser design
- AST structure
- Interpreter implementation
- Environment/symbol table
- Functions and scope
- Extension feature
- Error handling
- Testing strategy
- Major challenges encountered
- Lessons learned

*Include diagrams, screenshots, or examples where appropriate.*

---

## Recorded Video Demonstration

Instead of a live presentation, each group must create a recorded video demonstration of the completed programming language and interpreter.

- The video may be recorded using **YouTube**, **Microsoft Teams**, **Zoom**, **OBS Studio**, **Canvas Studio**, or another screen-recording platform.
- If YouTube is used, the video may be set to **Unlisted** so that it is accessible through the submitted link without being publicly searchable.

### Recommended Video Length

Your demonstration should be approximately **10–15 minutes**.
The recording should include both a technical explanation and a working demonstration of your interpreter.

### Your Video Must Demonstrate

#### 1. Introduction

Briefly introduce:

- Your group members
- The name of your programming language
- The purpose and major features of the language
- Your selected extension feature

#### 2. System Architecture

Explain the overall architecture:

```text
Source Code → Lexer → Tokens → Parser → AST → Interpreter → Output
```

Briefly explain the role of each component.

#### 3. Lexer Demonstration

Show a program written in your language and demonstrate how the lexer converts the source code into tokens. Explain some of the token types generated.

#### 4. Parser and AST Demonstration

Demonstrate how your parser processes the tokens and generates an AST. Use at least one expression that demonstrates operator precedence, such as:

```text
2 + 3 * 4
```

Explain why the AST represents multiplication before addition.

#### 5. Interpreter Demonstration

Run programs demonstrating:

- Variables
- Arithmetic expressions
- Print statements
- Comparisons
- `if`/`else`
- `while` loops
- Functions
- Parameters and return values
- Variable scope

#### 6. Extension Feature

Demonstrate the additional language feature developed by your group. Explain how the feature was incorporated into the language and interpreter.

#### 7. Error Handling

Demonstrate at least two different errors handled by your interpreter. Examples include:

- Invalid character
- Invalid syntax
- Undefined variable
- Division by zero

Explain how your interpreter detects and reports the errors.

#### 8. Code Walkthrough

Show important portions of your implementation and briefly explain how they work. At minimum, discuss:

- Lexer
- Parser
- AST
- Interpreter
- Environment/symbol table

*Do not simply scroll through the source code. Select important portions and explain their purpose.*

---

## Group Participation

- Every group member **must** participate in the recorded demonstration.
- Each student should clearly identify themselves and explain the components of the project they worked on.
- However, students are expected to understand the overall architecture of the complete interpreter, not only their individually assigned component.
- **A recording in which only one group member presents the entire project will not satisfy the group participation requirement.**

---

## AI Use Discussion

As part of the video, briefly discuss how your group used generative AI during development.

Explain:
1. Which AI tools you used
2. What types of tasks AI assisted with
3. One example where AI-generated code or advice required correction or modification
4. How your group verified that AI-generated code worked correctly

> **Purpose:** The purpose is not simply to list the AI tools used but to demonstrate that your group understands and takes responsibility for the resulting implementation.

Include the AI Use Statement in the written report as well as this discussion in the video.

---

## Video Submission

Submit either:
- A **YouTube video link**,
- A link to a recording hosted on another accessible platform, or
- A video file directly through Canvas if permitted.

> **Important:** Before submitting a video link, test the link in a private/incognito browser window to make sure the instructor can access it without requesting permission. Do not submit a link that requires the instructor to request access.

---

## Final Submission Checklist

Your Part 6 Canvas submission should include:

1. **Complete Project ZIP**
   ```text
   YourLanguage/
   │
   ├── lexer.py
   ├── parser.py
   ├── ast_nodes.py
   ├── interpreter.py
   ├── environment.py
   ├── main.py
   ├── tests/
   └── README.md
   ```
2. **Project Report:** Submit the 4–6 page report as a PDF or Word document.
3. **Recorded Demonstration:** Submit the accessible video link or recording.
4. **Test Programs:** Include at least 10 test programs with the project.
5. **Individual Contribution Statement:** Include a section in the project report that clearly identifies each student's contributions.
6. **AI Use Statement:** Include the required AI-use documentation in the final report.
7. **GitHub Link:** The GitHub link to your project.

---

## Grading Criteria (100 Points Total)

| Criterion | Points |
| :--- | :---: |
| Complete Working Interpreter | 25 |
| Integration & Correctness | 15 |
| Testing & Error Handling | 10 |
| Language/Extension Feature | 10 |
| Project Report & Documentation | 10 |
| Recorded Video Demonstration | 15 |
| Technical Explanation & Understanding | 10 |
| Individual Contributions & AI Use Documentation | 5 |
| **Total** | **100** |

---

## Important Notes

- The recorded demonstration is not simply a presentation of the final output. Your group must demonstrate that you understand how your programming language and interpreter work.
- The quality of the explanation, demonstration of working features, code walkthrough, and participation of all group members will be considered when grading.
