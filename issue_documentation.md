# Lab 5: Static Code Analysis

## Issue Documentation

| No. | Issue Identified | Tool | Severity/Type | Fix Applied |
|---|---|---|---|---|
| 1 | SQL query constructed using string formatting | Bandit | Medium – Security | Replaced string formatting with parameterized SQL query using `?` placeholders. |
| 2 | Mutable default argument `tags=[]` | Pylint | Bug risk | Changed default to `None` and initialized a new list inside the function. |
| 3 | Non-standard function names such as `registerPet()` | Pylint | Naming/style | Renamed functions to snake_case. |
| 4 | Constant name `adoption_count` was not uppercase | Pylint | Naming/style | Renamed it to `ADOPTION_COUNT`. |
| 5 | Missing module and function docstrings | Pylint | Documentation | Added descriptions to the module and functions. |
| 6 | Broad and bare exception handling | Pylint, Flake8, Bandit | Reliability/security | Removed unnecessary exception handlers and allowed unexpected errors to surface. |
| 7 | Use of `random.randint()` for adoption codes | Bandit | Low – Security | Replaced it with `secrets.randbelow()`. |
| 8 | Lines exceeding the permitted length | Pylint, Flake8 | Formatting | Split long statements across multiple lines. |
| 9 | Multiple statements on one line | Pylint, Flake8 | Formatting | Placed statements on separate lines. |
| 10 | String formatting could use an f-string | Pylint | Style | Used an f-string for adoption-code generation. |

## Verification Results

- Original Pylint score: 3.95/10
- Updated Pylint score: 9.71/10
- Bandit after fixes: No issues identified.
- Flake8 after fixes: No style violations.

## Reflection

Static code analysis helped identify code-quality, security, naming, documentation, and formatting issues without executing the code during the analysis. Pylint improved code quality, Bandit identified potential security risks, and Flake8 checked coding style. Fixing these issues made the program cleaner and easier to maintain.