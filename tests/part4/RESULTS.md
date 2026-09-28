# Part 4 Test Results

The interpreter was tested with five complete NovaLang programs. Expected and actual
outputs matched for all five functional tests.

## Functional tests

### 1. `test1_arithmetic.nova`
Expected:

20

Actual:

20

### 2. `test2_comparisons_if_else.nova`
Expected:
15

Actual:
15

### 3. `test3_while.nova`
Expected:

1
2
3
4
5

Actual:
1
2
3
4
5

### 4. `test4_combined.nova`
Expected:

1
2
4
6

Actual:

1
2
4
6


### 5. `test5_precedence.nova`
Expected:
15.0
14

Actual:
15.0
14


## Runtime-error tests

The interpreter also correctly raises:

- `Undefined variable 'missing'`
- `Division by zero`
- `if condition must evaluate to true or false`

The corresponding expected/actual semantic error messages are stored in the `outputs`
directory.
