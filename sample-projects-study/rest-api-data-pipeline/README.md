# REST API Data Pipeline

A comprehensive study project demonstrating REST API data fetching, parsing, and cleaning with both stateful and stateless approaches. Includes handling of large datasets with streaming capabilities.

## Features

- **Stateful Pipeline**: Maintains state across multiple data retrieval and processing operations
- **Stateless Pipeline**: Independent, idempotent data processing operations
- **Large Data Handling**: Memory-efficient streaming for large datasets
- **Comprehensive Logging**: File and console logging with structured output
- **Unit Tests**: Full test coverage for all components
- **Clean Code**: SOLID principles, defensive coding, and proper OOP design

## Project Structure

```
src/
├── api/              # REST API client classes
├── data/             # Data processing and cleaning modules
└── logging/          # Logging configuration

tests/               # Unit tests for all modules
```

## Installation

```bash
pip install -r requirements.txt
```

## Running Examples

```bash
# Run the CLI examples
python src/main.py --help

# Run tests
pytest tests/ -v

# Run with logging
python src/main.py --log-level DEBUG
```

## Key Concepts Demonstrated

1. **API Client Design**: Abstract base classes for HTTP clients
2. **Data Validation**: Type hints, defensive checks, and validation layers
3. **State Management**: Context managers for stateful operations
4. **Streaming**: Generator-based processing for large datasets
5. **Error Handling**: Custom exceptions and comprehensive error handling
6. **Testing**: Unit tests, mocking, and test fixtures

