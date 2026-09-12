### AI USE STATEMENT

**AI Tool(s) Used:** OpenAI Codex.

---

**How did your group use AI for this project milestone?**

Codex helped draft the Part 2 lexer, examples, tests, and run instructions from our Part 1 NovaLang design.

---

**Which project components received AI assistance?**

`lexer.py`, the six test programs and outputs, `tests/test_lexer.py`, and `README.md`.

---

**Describe at least one AI-generated suggestion, explanation, or code segment that your group modified, corrected, rejected, or improved.**

Codex considered broad `\w` and `\d` regex classes, then corrected that approach after checking our Part 1 grammar's ASCII limits. The lexer now uses explicit ASCII ranges, and a test confirms that `é` is rejected. Our group should review this decision before submission.

---

**How did your group test or independently verify AI-assisted work?**

The Part 1 EBNF was the reference. Codex ran six automated tests, compared every saved output with the CLI result, and checked the invalid-input exit status. Group members should rerun and review these checks before submission.

---

**What did your group learn from using AI during this milestone?**

A convenient regex can silently change the language; generated code must be checked against our own grammar.

---

**The purpose of this statement is to document how AI contributed to your development process and how your group evaluated its output.**
