"""Custom exceptions for Kafka module."""


class KafkaError(Exception):
    """Base exception for Kafka-related errors."""

    pass


class ProducerError(KafkaError):
    """Exception raised for producer-related errors."""

    pass


class ConsumerError(KafkaError):
    """Exception raised for consumer-related errors."""

    pass


class MessageValidationError(KafkaError):
    """Exception raised when message validation fails."""

    pass


class ConnectionError(KafkaError):
    """Exception raised for connection errors."""

    pass


class TimeoutError(KafkaError):
    """Exception raised when operation times out."""

    pass

