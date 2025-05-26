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
- Variable names follow snake_case.
- Avoid global variables when possible.
- Prefer list comprehensions and generator expressions for simple cases.
- Use built-in functions and standard library modules when possible.
- Keep functions small and focused on a single task.
- Write modular, reusable code.
- Remove unused imports and variables.
- Always include type annotations where applicable.
- Constants should be all-caps.
- Private variables should have prefix '_'

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

## Type Hints
- Use type hints for all new code (PEP 484)
- Annotate all function parameters and return values
- Use `Optional[T]` for nullable values
- Prefer `Union[T1, T2]` over `T1 | T2` for compatibility
- Use forward references (`"ClassName"`) for circular dependencies
- Use `typing` module constructs for complex types:
  - `List`, `Dict`, `Set`, `Tuple`
  - `Callable`, `Iterable`, `Mapping`
  - `Any`, `NoReturn`, etc.

## Error Handling
- Handle exceptions explicitly; avoid bare `except:` clauses.
- Use specific exception classes rather than bare exceptions
- Create custom exception classes for domain-specific errors
- Include relevant context in exception messages
- Use `raise ... from` for exception chaining (PEP 3134)
- Log exceptions appropriately before re-raising
- Consider error recovery paths where possible

## Logging
- Use the `logging` module instead of `print()`
- Configure logging at application entry point
- Use appropriate log levels:
  - DEBUG: Detailed debugging information
  - INFO: Normal operational messages
  - WARNING: Potential issues
  - ERROR: Serious problems
  - CRITICAL: Critical failures
- Include structured data in log messages when useful
- Avoid sensitive data in logs

## Formatting tools
- Use tools like `black` or `autopep8` for automatic code formatting.
- Use `flake8` or `pylint` for linting and code quality checks.


## References 
- [Khan Academy Style Guide](https://www.khanacademy.org/computing/intro-to-python-fundamentals/x5279a44ae0ab15d6:computational-thinking-with-variables/x5279a44ae0ab15d6:arithmetic-expressions/a/python-style-guide)  
- [Python Style Guide - UChicago](https://uchicago-cs.github.io/student-resource-guide/style-guide/python.html)
