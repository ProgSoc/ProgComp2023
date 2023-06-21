# Math Linting

A linter is a tool that analyzes source code to flag programming errors, bugs, syntax errors, etc. It's the red underline in your IDE when you misspell a word in your code.

You've decided to write a simple linter for math expressions, to help flag math expressions that are invalid. For now, you'll just decide whether or not the entire expression is valid, rather than which part of the expression is invalid.

A valid math expression is a series of numbers (such as `10`, `1.1`, `0.3`) and operators (`+`, `-`, `*`, `/`) separated by spaces. The expression will also have parentheses `(` and `)`.

Anything that is not a valid number and is not a valid operator/parenthese is considered invalid, and should error.

Numbers such as `1.1.1`, `1..1`, `.1` and `1.` are invalid, as are operators such as `++` and `+-`.

The `-` operator can only be used as a binary operator (e.g. `1 - 2`), or as a unary when at the beginning of an expression (e.g. `- 1 + 2` or `1 + ( - 2 )`).

# Input format

A single line containing a math expression, with all tokens being separated by spaces.

# Output format

Output `true` if the expression is valid, `false` otherwise.
