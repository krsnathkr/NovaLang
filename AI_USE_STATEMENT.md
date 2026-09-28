# AI Use Statement

## Part 4 AI Assistance

ChatGPT was used to help us during the development and testing of NovaLang Part 4.

We used AI assistance for the following tasks:

- Reviewing the code from Parts 1–3 before working on Part 4.
- Understanding how the interpreter works with the AST.
- Understanding how an environment or symbol table can store and retrieve variables.
- Adding support for `if/else` and `while` statements.
- Adding comparison operations.
- Adding runtime error handling.
- Creating and reviewing test programs.
- Checking the grammar and README documentation.
- Helping identify problems during testing.

We reviewed and tested the code instead of only relying on the generated suggestions.

## AI-Generated Suggestion That We Checked

One suggestion from ChatGPT was to use an `Environment` with a parent environment instead of using only one global dictionary for all variables.

The purpose of this approach was to allow blocks to have their own environment while still being able to access variables that were declared outside the block.

The implementation works in the following way:

1. A block can create a child environment.
2. Variable lookup first checks the current environment.
3. If the variable is not found, it checks the parent environment.
4. Assignment updates an existing variable in the environment where it was originally found.

We checked this behavior using the while-loop program:

let x = 1;

while (x <= 5) {
    print(x);
    x = x + 1;
}