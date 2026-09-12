CS 609 ADVANCED PROGRAMMING LANGUAGES
# FINAL PROJECT – PART 1: LANGUAGE DESIGN & GRAMMAR
## Programming Language: NovaLang
Group Members:
Sarada Garlapati
Krishna Jatin Thakar
Rabin Kc
# 1. Language Name and Brief Description
## 1.1 Language Name
NovaLang
## 1.2 Brief Description
NovaLang is a small general-purpose programming language designed for learning the fundamental concepts of programming language implementation and compiler construction.
NovaLang uses a clean and readable syntax inspired by languages such as C, Java, and JavaScript. It supports variables, numeric values, arithmetic expressions, comparison operators, conditional statements, loops, functions, return values, and basic variable scope.
The language is intentionally designed at a medium level of complexity. It provides the required features for the final project while keeping the syntax and grammar simple enough to implement within the project timeline.
A simple NovaLang program is shown below:
let x = 10;
let y = 20;

if (x < y) {
    print(x + y);
} else {
    print(x - y);
}
In this program, two variables are declared, their values are compared, and the appropriate result is printed.
# 2. List of Keywords
NovaLang uses the following reserved keywords:
These keywords are reserved and cannot be used as variable names or function names.
# 3. Operators and Delimiters
## 3.1 Arithmetic Operators

## 3.2 Comparison Operators
Comparison operations produce either true or false.
## 3.3 Logical Operators
NovaLang also supports logical operators as part of its extension feature.

## 3.4 Assignment Operator

## 3.5 Delimiters

# 4. Variable Declaration/Assignment Syntax
## 4.1 Variable Declaration
Variables are declared using the let keyword.
### Syntax
let variable = value;
### Examples
let x = 10;
let y = 20;
let price = 25.5;
A variable must be initialized when it is declared.
## 4.2 Variable Assignment
An existing variable can be assigned a new value using the = operator.
### Syntax
variable = expression;

### Examples
x = 20;
x = x + 5;
y = x * 2;


## 4.3 Variable Naming Rules
A variable name must begin with a letter or underscore. After the first character, it may contain letters, digits, and underscores.
### Valid identifiers
x
total
student_count
_value
marks1
### Invalid identifiers
1value
student-name
The keywords of NovaLang cannot be used as identifiers.
## 4.4 Numeric Values
NovaLang supports integer and decimal numeric values.
Examples:
10
25
1000
3.14
2.5
Example:
let x = 10;
let y = 2.5;
let result = x * y;

print(result);


# 5. Control-Structure Syntax
NovaLang provides if/else statements and while loops for controlling program execution.
## 5.1 If Statement
### Syntax
if (condition) {
    statements
}

### Example
let x = 15;

if (x > 10) {
    print(x);
}

The statements inside the block execute only when the condition evaluates to true.

## 5.2 If/Else Statement
### Syntax
if (condition) {
    statements
} else {
    statements
}

### Example
let age = 20;

if (age >= 18) {
    print(1);
} else {
    print(0);
}

The else block executes when the condition is false.

## 5.3 While Loop
### Syntax
while (condition) {
    statements
}

### Example
let i = 1;

while (i <= 5) {
    print(i);
    i = i + 1;
}

The loop repeatedly executes its block while the condition evaluates to true.

## 5.4 Operator Precedence
NovaLang follows the following operator precedence from highest to lowest:
For example:
let result = 10 + 5 * 2;

evaluates multiplication first, giving:
20

Parentheses can be used to change the evaluation order:
let result = (10 + 5) * 2;

which produces:
30




# 6. Function Syntax
NovaLang supports simple functions with parameters and return values.
## 6.1 Function Definition
### Syntax
fn functionName(parameter1, parameter2) {
    statements
    return expression;
}

### Example
fn add(a, b) {
    return a + b;
}

## 6.2 Function Parameters
A function may have zero or more parameters.
### Example with one parameter
fn square(x) {
    return x * x;
}

### Example with multiple parameters
fn multiply(a, b) {
    return a * b;
}


## 6.3 Function Call
A function is called by providing its name followed by parentheses.
add(10, 20);

A function call can also be used as part of an expression.
let result = add(10, 20);
print(result);

## 6.4 Return Statement
The return keyword is used to return a value from a function.
Example:
fn maximum(a, b) {
    if (a > b) {
        return a;
    } else {
        return b;
    }
}

The value returned by the function can be stored in a variable:
let result = maximum(10, 25);
print(result);


## 6.5 Function Scope
Function parameters and variables declared inside a function belong to the function's local scope.
Example:
fn calculate(x) {
    let result = x * 2;
    return result;
}

Here, x and result are local to the function.

# 7. At Least Three Complete Sample Programs
## Sample Program 1 – Arithmetic Operations
This program demonstrates variable declaration, assignment, arithmetic operations, operator precedence, and printing.
let a = 10;
let b = 5;

let sum = a + b;
let difference = a - b;
let product = a * b;
let quotient = a / b;

print(sum);
print(difference);
print(product);
print(quotient);

let result = (a + b) * 2;
print(result);

### Expected Output
15
5
50
2
30
## Sample Program 2 – If/Else and While Loop
This program demonstrates comparisons, the modulo operator, if/else, variable assignment, and a while loop.
let number = 7;

if (number % 2 == 0) {
    print(0);
} else {
    print(1);
}

let i = 1;

while (i <= 5) {
    print(i);
    i = i + 1;
}

### Expected Output
1
1
2
3
4
5

In this program, 1 represents an odd number and 0 represents an even number.

## Sample Program 3 – Functions and Boolean Conditions
This program demonstrates functions, parameters, return values, comparisons, Boolean expressions, and logical operators.
fn maximum(a, b) {
    if (a > b) {
        return a;
    } else {
        return b;
    }
}

fn isPositive(x) {
    return x > 0;
}

let x = 25;
let y = 40;

let largest = maximum(x, y);
print(largest);

let result = isPositive(x);

if (result && x < 100) {
    print(1);
} else {
    print(0);
}

### Expected Output
40
1


# 8. Initial BNF/EBNF Grammar
NovaLang will use EBNF (Extended Backus-Naur Form) to formally describe its syntax.
## 8.1 Program
<program> ::= { <statement> } ;

A program consists of zero or more statements.
## 8.2 Statement
<statement> ::=
      <variable-declaration>
    | <assignment>
    | <print-statement>
    | <if-statement>
    | <while-statement>
    | <function-definition>
    | <return-statement>
    | <expression-statement>
    ;

## 8.3 Variable Declaration
<variable-declaration> ::= "let" <identifier> "=" <expression> ";" ;


## 8.4 Assignment
<assignment> ::= <identifier> "=" <expression> ";" ;


## 8.5 Expression
<expression> ::= <logical-or> ;


## 8.6 Logical OR
<logical-or> ::= <logical-and> { "||" <logical-and> } ;


## 8.7 Logical AND
<logical-and> ::= <equality> { "&&" <equality> } ;


## 8.8 Equality
<equality> ::= <comparison> {
    ( "==" | "!=" ) <comparison>
} ;


## 8.9 Comparison
<comparison> ::= <term> {
    ( "<" | ">" | "<=" | ">=" ) <term>
} ;


## 8.10 Term
<term> ::= <factor> {
    ( "+" | "-" ) <factor>
} ;


## 8.11 Factor
<factor> ::= <unary> {
    ( "*" | "/" | "%" ) <unary>
} ;


## 8.12 Unary
<unary> ::=
      ( "!" | "-" ) <unary>
    | <primary>
    ;


## 8.13 Factor / Primary Expressions
<primary> ::=
      <number>
    | <boolean>
    | <identifier>
    | <function-call>
    | "(" <expression> ")"
    ;


## 8.14 Print Statement
<print-statement> ::= "print" "(" <expression> ")" ";" ;


## 8.15 If Statement
<if-statement> ::=
    "if" "(" <expression> ")" <block>
    [ "else" <block> ] ;


## 8.16 While Statement
<while-statement> ::=
    "while" "(" <expression> ")" <block> ;


## 8.17 Block
<block> ::= "{" { <statement> } "}" ;

Each block creates a new variable scope.

## 8.18 Function Definition
<function-definition> ::=
    "fn" <identifier> "(" [ <parameter-list> ] ")" <block> ;


## 8.19 Parameter List
<parameter-list> ::= <identifier> { "," <identifier> } ;


## 8.20 Return Statement
<return-statement> ::= "return" <expression> ";" ;


## 8.21 Expression Statement
<expression-statement> ::= <expression> ";" ;

This allows expressions such as function calls to be used as standalone statements.
Example:
add(10, 20);


## 8.22 Function Call
<function-call> ::= <identifier> "(" [ <argument-list> ] ")" ;


## 8.23 Argument List
<argument-list> ::= <expression> { "," <expression> } ;


## 8.24 Identifier
<identifier> ::= <letter> { <letter> | <digit> | "_" } ;


## 8.25 Letter
<letter> ::= "A" | ... | "Z" | "a" | ... | "z" | "_" ;


## 8.26 Digit
<digit> ::= "0" | "1" | "2" | "3" | "4"
          | "5" | "6" | "7" | "8" | "9" ;


## 8.27 Number
<number> ::= <integer> [ "." <digit> { <digit> } ] ;


## 8.28 Integer
<integer> ::= <digit> { <digit> } ;


## 8.29 Boolean
<boolean> ::= "true" | "false" ;


## 8.30 Complete EBNF Grammar
The complete initial grammar of NovaLang is:
<program> ::= { <statement> } ;

<statement> ::=
      <variable-declaration>
    | <assignment>
    | <print-statement>
    | <if-statement>
    | <while-statement>
    | <function-definition>
    | <return-statement>
    | <expression-statement>
    ;

<variable-declaration> ::= "let" <identifier> "=" <expression> ";" ;

<assignment> ::= <identifier> "=" <expression> ";" ;

<print-statement> ::= "print" "(" <expression> ")" ";" ;

<if-statement> ::=
    "if" "(" <expression> ")" <block>
    [ "else" <block> ] ;

<while-statement> ::=
    "while" "(" <expression> ")" <block> ;

<block> ::= "{" { <statement> } "}" ;

<function-definition> ::=
    "fn" <identifier> "(" [ <parameter-list> ] ")" <block> ;

<parameter-list> ::= <identifier> { "," <identifier> } ;

<return-statement> ::= "return" <expression> ";" ;

<expression-statement> ::= <expression> ";" ;

<expression> ::= <logical-or> ;

<logical-or> ::= <logical-and> { "||" <logical-and> } ;

<logical-and> ::= <equality> { "&&" <equality> } ;

<equality> ::= <comparison> {
    ( "==" | "!=" ) <comparison>
} ;

<comparison> ::= <term> {
    ( "<" | ">" | "<=" | ">=" ) <term>
} ;

<term> ::= <factor> {
    ( "+" | "-" ) <factor>
} ;

<factor> ::= <unary> {
    ( "*" | "/" | "%" ) <unary>
} ;

<unary> ::=
      ( "!" | "-" ) <unary>
    | <primary>
    ;

<primary> ::=
      <number>
    | <boolean>
    | <identifier>
    | <function-call>
    | "(" <expression> ")"
    ;

<function-call> ::= <identifier> "(" [ <argument-list> ] ")" ;

<argument-list> ::= <expression> { "," <expression> } ;

<identifier> ::= <letter> { <letter> | <digit> | "_" } ;

<number> ::= <integer> [ "." <digit> { <digit> } ] ;

<integer> ::= <digit> { <digit> } ;

<boolean> ::= "true" | "false" ;

<letter> ::= "A" | ... | "Z" | "a" | ... | "z" | "_" ;

<digit> ::= "0" | "1" | "2" | "3" | "4"
          | "5" | "6" | "7" | "8" | "9" ;


# 9. Proposed Additional/Extension Feature
## Boolean Values and Logical Operators
The additional feature proposed for NovaLang is Boolean values and logical operators.
NovaLang supports two Boolean values:
true
false

It also supports three logical operators:
&&
||
!

### Logical AND
condition1 && condition2

The result is true only when both conditions are true.
### Logical OR
condition1 || condition2

The result is true when at least one condition is true.
### Logical NOT
!condition

The result is the opposite Boolean value.
### Example
let age = 25;
let hasLicense = true;

if (age >= 18 && hasLicense) {
    print(1);
} else {
    print(0);
}

This feature was selected because it extends NovaLang's comparison and conditional capabilities without making the language unnecessarily complex.
It also provides an opportunity for the implementation to demonstrate Boolean evaluation and logical expression parsing.
# 10. Initial Responsibilities of Each Group Member
The initial responsibilities of the group members are divided as follows:
### Common Responsibilities
All group members will participate in:
GitHub repository management
Code development
Testing
Debugging
Code review
Integration
Documentation
Final project presentation
The responsibilities listed above are initial assignments and may be adjusted as the project progresses.

# 11. AI Use
AI tools were used as an assisting resource during the language design and grammar development phase of the project.
AI Tool Used: OpenAI ChatGPT
The AI tool was used for:
Brainstorming possible programming language names and syntax.
Developing the initial language structure.
Designing and refining the EBNF grammar.
Checking the consistency between language constructs and grammar rules.
Creating sample programs to demonstrate the proposed syntax.
Identifying possible implementation considerations.
The group members reviewed and modified the generated material according to the requirements of the project. The final language design and implementation decisions will be understood and verified by the group members.
AI was used as a supporting tool for brainstorming, grammar development, and documentation rather than as a replacement for the group's own understanding and implementation.

| Keyword | Purpose |
| --- | --- |
| let | Declares a variable |
| if | Defines a conditional statement |
| else | Defines the alternative branch of an if statement |
| while | Defines a while loop |
| fn | Defines a function |
| return | Returns a value from a function |
| print | Prints the result of an expression |
| true | Boolean true value |
| false | Boolean false value |


| Operator | Meaning | Example |
| --- | --- | --- |
| + | Addition | x + y |
| - | Subtraction | x - y |
| * | Multiplication | x * y |
| / | Division | x / y |
| % | Modulo | x % y |


| Operator | Meaning | Example |
| --- | --- | --- |
| == | Equal to | x == y |
| != | Not equal to | x != y |
| < | Less than | x < y |
| > | Greater than | x > y |
| <= | Less than or equal to | x <= y |
| >= | Greater than or equal to | x >= y |


| Operator | Meaning | Example |
| --- | --- | --- |
| && | Logical AND | x > 0 && x < 100 |
| ` |  | ` |
| ! | Logical NOT | !(x == 5) |


| Operator | Meaning | Example |
| --- | --- | --- |
| = | Assignment | x = 20; |


| Delimiter | Purpose |
| --- | --- |
| ( ) | Groups expressions and function parameters |
| { } | Defines blocks |
| , | Separates parameters and function arguments |
| ; | Terminates a statement |


| Precedence | Operators | Description |
| --- | --- | --- |
| 1 | () | Parentheses |
| 2 | !, unary - | Unary operations |
| 3 | *, /, % | Multiplication, division, modulo |
| 4 | +, - | Addition and subtraction |
| 5 | <, >, <=, >= | Relational comparison |
| 6 | ==, != | Equality comparison |
| 7 | && | Logical AND |
| 8 | ` |  |


| Group Member | Initial Responsibility |
| --- | --- |
| Sarada Garlapati | Language syntax, keywords, operators, delimiters, and lexical analysis design |
| Krishna Jatin Thakar | EBNF grammar and parser design |
| Rabin Kc | Variables, expressions, scope, and semantic analysis |
| Sarada&Krishna& Rabin | Control structures, functions, sample programs, and documentation |
