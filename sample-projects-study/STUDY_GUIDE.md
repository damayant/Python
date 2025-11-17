# Python Development Study Guide

A comprehensive collection of four repositories for mastering Python development, REST APIs, messaging systems, and coding best practices.

## 📚 Repository Overview

### 1. **rest-api-data-pipeline** ⚙️
Master REST API development with focus on data processing pipelines.

**Key Topics:**
- Stateless vs Stateful API clients
- Data validation and cleaning
- Streaming large datasets with generators
- Memory-efficient processing
- Logging configuration (console & file)
- Comprehensive unit tests

**Directory Structure:**
```
rest-api-data-pipeline/
├── src/
│   ├── api/          # REST API clients
│   ├── data/         # Data processing & validation
│   └── logging/      # Logging configuration
├── tests/            # Unit tests
└── requirements.txt
```

**Key Classes:**
- `StatelessAPIClient` - Independent HTTP requests
- `StatefulAPIClient` - Maintains session state, retry logic
- `DataProcessor` - In-memory processing
- `StreamingDataProcessor` - Generator-based large data processing
- `DataValidator` - Data validation and cleaning

**Learning Focus:**
- Abstract base classes (ABC)
- Generator functions for memory efficiency
- Context managers
- Error handling strategies
- Design patterns: Factory, Decorator
- Unit testing with mocking

---

### 2. **rest-api-simple-projects** 🏗️
Compare procedural vs Object-Oriented approaches to REST API development.

**Key Topics:**
- Functional (procedural) approach
- OOP approach with service layer
- Design patterns (Repository, Service)
- Dependency injection
- Testability comparison
- SOLID principles application

**Directory Structure:**
```
rest-api-simple-projects/
├── without_oop/      # Procedural Flask API
├── with_oop/         # OOP Flask API
├── tests/            # Unit tests
└── requirements.txt
```

**Without OOP (Procedural):**
- Module-level functions
- Global state management
- Direct state mutation
- Limited reusability

**With OOP:**
- Repository pattern for data access
- Service layer for business logic
- Dependency injection
- Easy to test with mocks
- High reusability

**Learning Focus:**
- Service layer pattern
- Repository pattern
- Dependency injection
- Testing strategies
- Separation of concerns
- Code organization

---

### 3. **kafka-producer-consumer** 📨
Master Apache Kafka message queue integration in Python.

**Key Topics:**
- Kafka producer with error handling & retries
- Kafka consumer with offset management
- Message serialization/deserialization
- Configuration management
- Type safety with Pydantic
- Comprehensive error handling
- Thread-safe operations

**Directory Structure:**
```
kafka-producer-consumer/
├── src/
│   └── kafka/
│       ├── producer.py       # Message producer
│       ├── consumer.py       # Message consumer
│       ├── config.py         # Configuration
│       └── exceptions.py     # Custom exceptions
├── tests/                    # Unit tests
├── examples/                 # Usage examples
└── requirements.txt
```

**Key Classes:**
- `KafkaProducerService` - Send messages with batching
- `KafkaConsumerService` - Consume with offset management
- `KafkaConfig` - Configuration with environment variables

**Features:**
- Batch message processing
- Retry logic with exponential backoff
- Custom serialization/deserialization
- Context manager support
- Comprehensive logging
- Full type hints

**Learning Focus:**
- Message queue patterns
- Producer-consumer architecture
- Error handling & retries
- Configuration management
- Testing with mocking
- Resource management

---

### 4. **python-coding-style** 📖
Comprehensive study of Python coding standards, best practices, and design patterns.

**Key Topics:**
- Naming conventions (PEP 8)
- Type hints and annotations
- Documentation and docstrings
- Error handling strategies
- Defensive coding practices
- Anti-patterns to avoid
- SOLID principles
- Design patterns

**Directory Structure:**
```
python-coding-style/
├── src/
│   ├── good_practices/
│   │   ├── naming_conventions.py
│   │   ├── type_hints.py
│   │   ├── error_handling.py
│   │   └── defensive_coding.py
│   ├── anti_patterns/
│   │   └── code_smells.py
│   └── design_patterns/
│       ├── singleton.py
│       └── factory.py
├── tests/                    # Unit tests
└── requirements.txt
```

**Good Practices:**
- PascalCase for classes
- snake_case for functions & variables
- UPPER_CASE for constants
- Private attributes with underscore prefix
- Comprehensive type hints
- Detailed docstrings
- Specific exception handling
- Input validation (defensive)

**Anti-Patterns (Things to Avoid):**
- ❌ Magic numbers without constants
- ❌ God objects with too many responsibilities
- ❌ Deep nesting (arrow anti-pattern)
- ❌ Mutable default arguments
- ❌ Bare except clauses
- ❌ Silent failures
- ❌ Missing documentation
- ❌ Very long functions

**Design Patterns Covered:**
- **Singleton:** One instance, global access
  - Decorator approach
  - Metaclass approach
  - Thread-safe singleton
- **Factory:** Create objects without specifying classes
  - Simple factory
  - Abstract factory

**Learning Focus:**
- PEP 8 compliance
- Code readability
- Maintainability
- Testability
- SOLID principles
- Python idioms

---

## 🎯 SOLID Principles Implementation

### Single Responsibility Principle (SRP)
Each class has one reason to change:
- `DatabaseConnection` only manages connections
- `EmailService` only sends emails
- `DataValidator` only validates data

### Open/Closed Principle (OCP)
Open for extension, closed for modification:
- `DatabaseFactory` allows adding new drivers without changing existing code
- Abstract base classes define extension points

### Liskov Substitution Principle (LSP)
Subtypes must be substitutable for base types:
- All database drivers implement `DatabaseDriver` interface
- Can swap `MySQLDriver` for `PostgreSQLDriver` without issues

### Interface Segregation Principle (ISP)
Clients depend on specific interfaces:
- `Repository` interface provides only necessary methods
- Clients only see what they need

### Dependency Inversion Principle (DIP)
Depend on abstractions, not concretions:
- `BookService` depends on `Repository` abstraction
- Can inject `InMemoryRepository` or `DatabaseRepository`

---

## 🧪 Testing Across All Projects

### Unit Testing Framework: pytest

**Testing Practices:**
- ✓ Test fixtures for setup
- ✓ Mocking external dependencies
- ✓ Test coverage reporting
- ✓ Parameterized tests
- ✓ Test data factories

**Running Tests:**
```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src

# Run specific test file
pytest tests/test_api_client.py -v

# Run specific test class
pytest tests/test_api_client.py::TestStatelessAPIClient -v
```

---

## 📋 Best Practices Summary

### Code Organization
✓ Logical module structure
✓ Clear separation of concerns
✓ Reusable components
✓ Package-based organization

### Naming
✓ Descriptive names
✓ Follow PEP 8 conventions
✓ Avoid abbreviations
✓ Use domain language

### Type Safety
✓ Add type hints to all public functions
✓ Use generic types for collections
✓ Use Optional for nullable values
✓ Use Union for multiple types

### Documentation
✓ Module docstrings
✓ Function/method docstrings with Args, Returns, Raises
✓ Class docstrings with Attributes
✓ Inline comments for complex logic

### Error Handling
✓ Raise specific exceptions
✓ Provide meaningful error messages
✓ Log errors with context
✓ Use defensive checks
✓ Validate inputs

### Defensive Coding
✓ Type validation
✓ Range validation
✓ Null/empty checks
✓ State validation
✓ Defensive copying

---

## 🚀 Learning Path

### Phase 1: Fundamentals (Coding Style)
1. Start with `python-coding-style/good_practices/`
   - Learn naming conventions
   - Understand type hints
   - Study error handling
   - Practice defensive coding

2. Study anti-patterns to recognize and avoid them
3. Learn design patterns (Singleton, Factory)

### Phase 2: API Development (Simple Projects)
1. Review `rest-api-simple-projects/without_oop/`
   - Understand functional approach
   - Identify limitations

2. Study `rest-api-simple-projects/with_oop/`
   - Learn service layer pattern
   - Understand repository pattern
   - See dependency injection in action

### Phase 3: Advanced API Concepts (Data Pipeline)
1. Master `rest-api-data-pipeline/`
   - Understand stateless vs stateful clients
   - Learn streaming for large data
   - Study advanced logging
   - Master error handling

### Phase 4: Message Queue Integration (Kafka)
1. Learn `kafka-producer-consumer/`
   - Understand producer pattern
   - Master consumer pattern
   - Learn retry strategies
   - Study configuration management

---

## 🔧 Installation & Setup

### Install All Dependencies
```bash
cd /Users/damayantighosh/Documents/workspace/cursor-projects-study

# Install each project's dependencies
for repo in rest-api-data-pipeline rest-api-simple-projects kafka-producer-consumer python-coding-style; do
    echo "Installing $repo dependencies..."
    pip install -r $repo/requirements.txt
done
```

### Run Tests
```bash
# Test rest-api-data-pipeline
pytest rest-api-data-pipeline/tests/ -v --cov

# Test rest-api-simple-projects
pytest rest-api-simple-projects/tests/ -v --cov

# Test kafka-producer-consumer
pytest kafka-producer-consumer/tests/ -v --cov

# Test python-coding-style
pytest python-coding-style/tests/ -v --cov
```

---

## 📚 Key Concepts Reference

### REST APIs
- Stateless vs Stateful clients
- Pagination handling
- Error responses
- Request/Response serialization
- Session management

### Data Processing
- Validation
- Cleaning/Transformation
- In-memory vs streaming
- Generator functions
- Batch processing

### Message Queues
- Producer-Consumer pattern
- Serialization
- Error handling & retries
- Offset management
- Consumer groups

### Design Patterns
- Singleton: One instance
- Factory: Object creation
- Repository: Data access abstraction
- Service: Business logic
- Decorator: Behavior modification

### SOLID Principles
- SRP: One responsibility
- OCP: Extensible without modification
- LSP: Substitutable subtypes
- ISP: Specific interfaces
- DIP: Depend on abstractions

---

## 🔍 Code Quality Tools

### Linting and Formatting
```bash
# Run pylint
pylint src/

# Format code with black
black src/

# Type checking with mypy
mypy src/

# Run all checks
pytest && black --check . && pylint src/
```

---

## 📝 Notes for Advanced Study

1. **Concurrency**: Extend Kafka examples with threading/async
2. **Caching**: Add caching layer to API clients
3. **Rate Limiting**: Implement rate limiting in producers
4. **Database Persistence**: Replace in-memory storage with actual DB
5. **Authentication**: Add OAuth/JWT to REST APIs
6. **API Documentation**: Generate OpenAPI/Swagger docs
7. **Performance**: Profile and optimize bottlenecks
8. **Monitoring**: Add metrics and health checks

---

## 🎓 Summary

These four repositories provide a comprehensive education in:
- ✓ Python coding standards and best practices
- ✓ REST API design and implementation
- ✓ Data pipeline creation and processing
- ✓ Message queue integration
- ✓ Design patterns and SOLID principles
- ✓ Unit testing and quality assurance
- ✓ Error handling and logging
- ✓ Defensive coding practices

Use them as reference for your own projects and to continuously improve your Python development skills!

