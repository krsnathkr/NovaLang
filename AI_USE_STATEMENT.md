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

## Part 4 AI-Generated Suggestion That We Checked

One suggestion from ChatGPT was to use an `Environment` with a parent environment instead of using only one global dictionary for all variables.

The purpose of this approach was to allow blocks to have their own environment while still being able to access variables that were declared outside the block.

The implementation works in the following way:

1. A block can create a child environment.
2. Variable lookup first checks the current environment.
3. If the variable is not found, it checks the parent environment.
4. Assignment updates an existing variable in the environment where it was originally found.

We checked this behavior using a while-loop program where a variable declared outside the loop was updated inside the loop. The program produced the expected result.

## Part 5 AI Assistance

ChatGPT was also used during the development and testing of Part 5.

AI assistance was used for:

- Reviewing the existing Part 4 code before adding new features.
- Adding AST nodes for function definitions, function calls, and return statements.
- Extending the parser to recognize function definitions, parameters, arguments, function calls, and return statements.
- Adding the `function` keyword to the lexer.
- Understanding how local and global scope should work with functions.
- Implementing function calls and return values in the interpreter.
- Implementing and testing recursion as the Part 5 extension feature.
- Creating and reviewing Part 5 test programs.
- Updating the EBNF grammar.
- Reviewing the README and project documentation.

All suggested changes were tested before being accepted. We also reran the Part 4 tests after making Part 5 changes to make sure the new features did not break the previous interpreter.

## Part 5 AI-Generated Suggestion That We Verified

One suggestion from ChatGPT was to create a new local environment every time a function is called. The local environment uses the function's defining environment as its parent.

We verified this suggestion with the following scope behavior:

let x = 10;

function test() {
    let x = 20;
    print(x);
}
test();
print(x);


The program produced:
20
10

This confirmed that the variable inside the function was local and did not replace the global variable.

We also tested this environment design with recursion. We created a recursive factorial function and called `factorial(5)`. The program returned:

120

This helped verify that each recursive function call received its own local environment and parameter value.

## Part 6 AI Assistance

For final integration, GPT-6.1 Sol supported implementation and test work, GPT-6 Luna prepared documentation, and GPT-6 Astra advised on design and review. AI assistance covered cumulative design review, the command-line entry point, regression and feature tests, the README, report, and demonstration guide. The human group members remain responsible for reviewing the code and report, recording the demonstration, and explaining their contributions.

Integration exposed two concrete failures. On Python 3.9.6, evaluating a `BlockNode | None` annotation prevented module import; postponed annotation evaluation fixed it. The default recursive `unittest` discovery also missed tests in nested directories; package markers and test adapters made the cumulative checks discoverable. The implementation retained the original Part 1 `fn` spelling, accepted the later Part 5 `function` spelling, and restored general expression statements. The implementation agent then ran 64 tests, compiled the project, and compared expected and actual output for all 25 Part 6 valid/error programs. The group should review those results before submission.

The earlier Part 4 and Part 5 statements above remain as the historical AI-use record for those milestones. They describe checks recorded at those times and do not by themselves establish Part 6 verification or completion.

## Testing and Verification

For Part 5, we created six new test programs covering:

- Basic function definitions and calls
- Parameters
- Return values
- Local variables
- Local and global scope
- Access to outer variables
- Recursion
- Multiple calls to the same function

We ran the Part 5 automated tests and all 6 tests passed.

We also ran the Part 4 and Part 5 tests together. All 10 tests passed, confirming that the Part 5 changes did not break the Part 4 functionality.
