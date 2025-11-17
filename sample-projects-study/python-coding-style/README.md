# Python Coding Style Guide

A comprehensive study of Python coding standards, best practices, anti-patterns, and design patterns with practical examples.

## Contents

### Good Practices (`src/good_practices/`)
- **naming_conventions.py**: Proper naming conventions
- **type_hints.py**: Type hints and annotations
- **documentation.py**: Docstrings and comments
- **error_handling.py**: Proper exception handling
- **defensive_coding.py**: Defensive programming techniques

### Anti-Patterns (`src/anti_patterns/`)
- **naming_anti_patterns.py**: Common naming mistakes
- **type_anti_patterns.py**: Type-related anti-patterns
- **error_anti_patterns.py**: Poor error handling
- **code_smells.py**: Code smells and bad practices

### Design Patterns (`src/design_patterns/`)
- **singleton.py**: Singleton pattern
- **factory.py**: Factory pattern
- **observer.py**: Observer pattern
- **decorator.py**: Decorator pattern
- **context_managers.py**: Context manager pattern

## Key Topics

1. **SOLID Principles**
   - Single Responsibility
   - Open/Closed
   - Liskov Substitution
   - Interface Segregation
   - Dependency Inversion

2. **Code Quality**
   - PEP 8 compliance
   - Code readability
   - Maintainability
   - Testability

3. **Python Idioms**
   - Context managers
   - Generators
   - Decorators
   - Properties
   - Magic methods

4. **Design Patterns**
   - Creational patterns
   - Structural patterns
   - Behavioral patterns

## Installation

```bash
pip install -r requirements.txt
```

## Running Examples

```bash
# Good practices examples
python examples/good_practices_example.py

# Anti-patterns examples (showing what NOT to do)
python examples/anti_patterns_example.py

# Design patterns examples
python examples/design_patterns_example.py
```

## Running Tests

```bash
pytest tests/ -v --cov=src
```

## Learning Path

1. Start with naming conventions and documentation
2. Learn type hints and documentation
3. Study error handling approaches
4. Explore defensive coding practices
5. Learn anti-patterns to avoid
6. Study design patterns for solutions
7. Apply SOLID principles

## Best Practices Summary

✓ Use meaningful, descriptive names
✓ Add type hints for all public functions
✓ Write comprehensive docstrings
✓ Use exceptions for error handling
✓ Validate inputs defensively
✓ Keep functions focused and small
✓ Use context managers for resource management
✓ Follow PEP 8 style guide
✓ Write testable code
✓ Use design patterns for common problems

