# REST API Simple Projects

Demonstrates building REST APIs with and without Object-Oriented Programming principles. Perfect for comparing procedural vs OOP approaches.

## Projects Included

### 1. Without OOP (Procedural Approach)
- Simple Flask API using functional programming
- Direct state management
- Module-level functions
- File: `without_oop/app.py`

### 2. With OOP (Object-Oriented Approach)
- Flask API using classes and inheritance
- Encapsulation and abstraction
- Service layer pattern
- File: `with_oop/app.py`

## Features

Both implementations include:
- REST endpoints for CRUD operations
- Input validation and error handling
- Comprehensive logging
- Unit tests
- Request/response serialization
- Error handling middleware

## Installation

```bash
pip install -r requirements.txt
```

## Running Examples

### Without OOP
```bash
python without_oop/app.py
```

### With OOP
```bash
python with_oop/app.py
```

## Running Tests
```bash
pytest tests/ -v --cov
```

## Key Differences

| Aspect | Without OOP | With OOP |
|--------|------------|----------|
| Code Organization | Functions | Classes |
| State Management | Module-level | Instance attributes |
| Extensibility | Limited | High |
| Testing | Mocking functions | Dependency injection |
| Reusability | Lower | Higher |

## Learning Outcomes

- Understand the benefits of OOP in API development
- Learn design patterns like Repository, Service Layer
- Understand dependency injection and composition
- Compare code maintainability and testability

