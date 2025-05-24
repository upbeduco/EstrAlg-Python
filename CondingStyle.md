# Coding Style and Best Practices for Python Development

## Code documentation
- Write brief clear docstrings documenting classes, methods, functions.
- Follow [PEP 257](https://peps.python.org/pep-0257/) conventions for docstrings.
- Include parameter and return type descriptions where helpful.

## General code
- Use pythonic constructs where applicable.
- Follow [PEP 8](https://peps.python.org/pep-0008/) for code style and formatting.
- Use 4 spaces per indentation level; **never use tabs**.
- Limit lines to 79 characters.
- Use meaningful variable, function, and class names.
- Avoid global variables when possible.
- Prefer list comprehensions and generator expressions for simple cases.
- Use built-in functions and standard library modules when possible.
- Handle exceptions explicitly; avoid bare `except:` clauses.
- Keep functions small and focused on a single task.
- Write modular, reusable code.
- Remove unused imports and variables.

## Imports
- Place all imports at the top of the file.
- Group imports in the following order: standard library, third-party, local application.
- Use absolute imports rather than relative imports.

## Comments
- Write comments to explain why, not what.
- Update comments when code changes.
- Use inline comments sparingly and only when necessary.

## Testing
- Write unit tests for all new code.
- Use descriptive names for test functions.
- Prefer pytest or unittest frameworks.

## Version control
- Commit small, focused changes with clear commit messages.
- Do not commit secrets or sensitive data.

## Type hints
- Use type hints for function signatures and variable declarations where appropriate.

## Formatting tools
- Use tools like `black` or `autopep8` for automatic code formatting.
- Use `flake8` or `pylint` for linting and code quality checks.



