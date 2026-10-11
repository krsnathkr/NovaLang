# NovaLang Token Definitions

The lexer returns each token's type, source lexeme, line, and column. Whitespace is skipped. The tables below describe the token types recognized by `lexer.py`.

| Token type | Lexeme or rule | Meaning |
| --- | --- | --- |
| `LET` | `let` | Variable declaration keyword |
| `PRINT` | `print` | Output statement keyword |
| `IF` | `if` | Conditional keyword |
| `ELSE` | `else` | Alternative branch keyword |
| `WHILE` | `while` | Loop keyword |
| `FN` | `fn` | Function definition keyword |
| `FUNCTION` | `function` | Function definition keyword accepted for compatibility |
| `RETURN` | `return` | Function return keyword |
| `TRUE` | `true` | Boolean literal |
| `FALSE` | `false` | Boolean literal |
| `ID` | `[A-Za-z_][A-Za-z0-9_]*` | Identifier |
| `NUMBER` | `[0-9]+(\.[0-9]+)?` | Integer or decimal numeric literal |
| `EQUAL_EQUAL` | `==` | Equality comparison |
| `BANG_EQUAL` | `!=` | Inequality comparison |
| `LESS_EQUAL` | `<=` | Less-than-or-equal comparison |
| `GREATER_EQUAL` | `>=` | Greater-than-or-equal comparison |
| `AND_AND` | `&&` | Logical AND |
| `OR_OR` | `||` | Logical OR |
| `PLUS` | `+` | Addition |
| `MINUS` | `-` | Subtraction or unary negation |
| `STAR` | `*` | Multiplication |
| `SLASH` | `/` | Division |
| `PERCENT` | `%` | Remainder |
| `LESS` | `<` | Less-than comparison |
| `GREATER` | `>` | Greater-than comparison |
| `BANG` | `!` | Logical NOT |
| `ASSIGN` | `=` | Assignment |
| `LPAREN` / `RPAREN` | `(` / `)` | Parentheses |
| `LBRACE` / `RBRACE` | `{` / `}` | Block braces |
| `COMMA` | `,` | Parameter or argument separator |
| `SEMICOLON` | `;` | Statement terminator |

The reserved words are `let`, `print`, `if`, `else`, `while`, `fn`, `function`, `return`, `true`, and `false`. Identifiers begin with an ASCII letter or underscore and continue with ASCII letters, digits, or underscores. The lexer scans the complete identifier before checking whether it is a reserved word, so a longer name such as `letdown_2` is one `ID` token.

The lexer checks two-character operators before one-character operators. A minus sign is always a separate `MINUS` token; it is not part of a number token. Invalid characters and malformed numeric literals raise a lexical error with a source location. The lexer does not emit an end-of-file token.
