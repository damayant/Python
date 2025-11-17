# Kafka Producer-Consumer

Comprehensive study of Kafka message queue with producer and consumer implementations following SOLID principles and best practices.

## Features

- **Producer**: Send messages to Kafka topics with error handling and retries
- **Consumer**: Read messages from topics with offset management
- **Error Handling**: Comprehensive error handling and logging
- **Type Safety**: Full type hints and validation
- **Testing**: Unit tests with mocking
- **Configuration**: Environment-based configuration
- **OOP Design**: Clean architecture with service layer pattern

## Architecture

```
src/
├── kafka/
│   ├── producer.py    # Message producer
│   ├── consumer.py    # Message consumer
│   ├── config.py      # Configuration
│   └── exceptions.py  # Custom exceptions
└── models/
    ├── message.py     # Message model
    └── event.py       # Event definitions
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Producer

```python
from src.kafka.producer import KafkaProducerService

producer = KafkaProducerService(
    bootstrap_servers=['localhost:9092'],
    topic='my-topic'
)

producer.send_message({'key': 'value'})
producer.close()
```

### Consumer

```python
from src.kafka.consumer import KafkaConsumerService

consumer = KafkaConsumerService(
    bootstrap_servers=['localhost:9092'],
    topic='my-topic',
    group_id='my-group'
)

for message in consumer.consume(timeout_ms=1000):
    print(f"Received: {message}")

consumer.close()
```

## Testing

```bash
pytest tests/ -v --cov
```

## Key Concepts Demonstrated

1. **Producer Design**: Batch processing, retries, partitioning
2. **Consumer Design**: Consumer groups, offset management, error handling
3. **Message Serialization**: JSON encoding/decoding
4. **Configuration Management**: Environment variables and config classes
5. **Error Handling**: Custom exceptions and retry logic
6. **Logging**: Structured logging for debugging
7. **Testing**: Mocking Kafka clients

