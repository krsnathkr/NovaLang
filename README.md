# NovaLang
NovaLang is our group programming language project for CS 609. We have been developing this project step by step throughout the semester. In the previous parts, we worked on the language design, lexer, parser, AST, and interpreter. In Part 5, we extended the language by adding functions, variable scope, and recursion.

## Project Progress

- Part 1: Language design and grammar
- Part 2: Lexer
- Part 3: Parser and AST
- Part 4: Interpreter and environment/symbol table
- Part 5: Functions, scope, and recursion

## Part 4

For Part 4, we added the interpreter and environment to our previous project. The interpreter reads the AST created by the parser and executes the program.

The following features are supported:

- Variable declaration
- Variable assignment
- Addition, subtraction, multiplication, and division
- Modulo operation
- Operator precedence
- Parentheses
- Comparison operators
- Boolean values
- Logical operators
- If/else statements
- While loops
- Print statements
- Runtime error handling

The comparison operators supported are:

`==`, `!=`, `<`, `>`, `<=`, `>=`

The logical operators supported are:

`&&`, `||`, `!`

## Part 5

For Part 5, we extended the interpreter to support functions and variable scope. Functions can have parameters, local variables, function calls, and return values.

Example:

function add(a, b) {
    return a + b;
}
let result = add(10, 20);
print(result);


The output is:
30

### Variable Scope
NovaLang uses environments to represent variable scope. Each function call creates its own local environment. The function environment has a parent environment, which allows a function to access variables from an outer scope when needed.
Local variables are stored in the function's local environment, so they do not replace variables with the same name in the global environment.

For example:
let x = 10;
function test() {
    let x = 20;
    print(x);
}
test();
print(x);

The output is:
20
10

This shows that the `x` inside the function is local while the global `x` remains unchanged.

### Extension Feature: Recursion

For our Part 5 extension feature, we implemented recursion. A function can call itself while it is executing.

For example:
function factorial(n) {
    if (n <= 1) {
        return 1;
    }

    return n * factorial(n - 1);
}

print(factorial(5));

The output is:

120

Each recursive function call creates a new local environment. This keeps the parameter values from different calls separate.

## Part 5 Testing

We created six new programs for Part 5:

1. Basic function definition and call
2. Function parameters and local variables
3. Local and global variable scope
4. Function access to an outer variable
5. Recursive factorial function
6. Multiple calls to the same function

The Part 5 tests can be run with:

       python3 -m pytest tests/part5/ -v

Part 4 and Part 5 can be tested together with:

       python3 -m pytest tests/part4/ tests/part5/ -v

At the time of our Part 5 testing, all 10 Part 4 and Part 5 automated tests passed.

## Running a NovaLang Program

A NovaLang program can be executed with:

      python3 interpreter.py path/to/program.nova

For example:
    python3 interpreter.py tests/part5/programs/test5_recursion.nova

## Project Files

The main files used in the project are:

- `lexer.py`
- `parser.py`
- `ast_nodes.py`
- `environment.py`
- `interpreter.py`
- `grammar.ebnf`
- `README.md`
- `AI_USE_STATEMENT.md`
- `tests/part4/`
- `tests/part5/`