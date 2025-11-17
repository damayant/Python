"""Kafka producer implementation."""

import json
import logging
import time
from typing import Any, Dict, Optional

from kafka import KafkaProducer
from kafka.errors import KafkaError as LibKafkaError

from .config import KafkaConfig
from .exceptions import ProducerError


class KafkaProducerService:
    """Service for sending messages to Kafka topics."""

    def __init__(
        self,
        config: Optional[KafkaConfig] = None,
        bootstrap_servers: Optional[list] = None,
        topic: Optional[str] = None,
    ):
        """Initialize Kafka producer service.

        Args:
            config: KafkaConfig instance
            bootstrap_servers: List of bootstrap servers (overrides config)
            topic: Kafka topic (overrides config)

        Raises:
            ProducerError: If initialization fails
        """
        self.logger = logging.getLogger(self.__class__.__name__)

        # Use provided config or create default
        if config is None:
            config = KafkaConfig()

        # Override with provided parameters
        if bootstrap_servers:
            config.bootstrap_servers = bootstrap_servers
        if topic:
            config.topic = topic

        self.config = config
        self.topic = config.topic

        if not self.topic:
            raise ProducerError("Topic must be specified")

        self._producer = self._create_producer()
        self.logger.info(f"KafkaProducerService initialized for topic: {self.topic}")

    def _create_producer(self) -> KafkaProducer:
        """Create Kafka producer instance.

        Returns:
            KafkaProducer instance

        Raises:
            ProducerError: If producer creation fails
        """
        try:
            producer = KafkaProducer(
                bootstrap_servers=self.config.bootstrap_servers,
                value_serializer=self._serialize_value,
                key_serializer=self._serialize_key,
                retries=self.config.retries,
                retry_backoff_ms=self.config.retry_backoff_ms,
                request_timeout_ms=self.config.request_timeout_ms,
            )
            self.logger.debug("KafkaProducer instance created successfully")
            return producer

        except LibKafkaError as e:
            error_msg = f"Failed to create KafkaProducer: {str(e)}"
            self.logger.error(error_msg)
            raise ProducerError(error_msg)

    @staticmethod
    def _serialize_key(key: Optional[Any]) -> Optional[bytes]:
        """Serialize message key.

        Args:
            key: Message key

        Returns:
            Serialized key bytes
        """
        if key is None:
            return None

        if isinstance(key, bytes):
            return key

        if isinstance(key, str):
            return key.encode("utf-8")

        return json.dumps(key).encode("utf-8")

    @staticmethod
    def _serialize_value(value: Any) -> bytes:
        """Serialize message value.

        Args:
            value: Message value

        Returns:
            Serialized value bytes

        Raises:
            ProducerError: If serialization fails
        """
        try:
            if isinstance(value, bytes):
                return value

            if isinstance(value, str):
                return value.encode("utf-8")

            if isinstance(value, dict):
                return json.dumps(value).encode("utf-8")

            return json.dumps(value).encode("utf-8")

        except (TypeError, ValueError) as e:
            raise ProducerError(f"Failed to serialize value: {str(e)}")

    def send_message(
        self,
        value: Any,
        key: Optional[Any] = None,
        topic: Optional[str] = None,
        timeout_ms: int = 10000,
    ) -> Dict[str, Any]:
        """Send a message to Kafka topic.

        Args:
            value: Message value (will be JSON serialized if dict)
            key: Message key (optional)
            topic: Topic to send to (overrides default)
            timeout_ms: Timeout for send operation

        Returns:
            Dictionary with send metadata

        Raises:
            ProducerError: If send fails
        """
        target_topic = topic or self.topic

        if not target_topic:
            raise ProducerError("Topic must be specified")

        try:
            self.logger.debug(f"Sending message to topic: {target_topic}")

            # Send message asynchronously
            future = self._producer.send(
                target_topic,
                value=value,
                key=key,
            )

            # Wait for send to complete
            record_metadata = future.get(timeout_secs=timeout_ms / 1000)

            metadata = {
                "topic": record_metadata.topic,
                "partition": record_metadata.partition,
                "offset": record_metadata.offset,
                "timestamp": record_metadata.timestamp,
                "success": True,
            }

            self.logger.info(
                f"Message sent successfully to topic {target_topic}, "
                f"partition {record_metadata.partition}, "
                f"offset {record_metadata.offset}"
            )

            return metadata

        except LibKafkaError as e:
            error_msg = f"Failed to send message to {target_topic}: {str(e)}"
            self.logger.error(error_msg)
            raise ProducerError(error_msg)

    def send_batch(
        self,
        messages: list[Dict[str, Any]],
        topic: Optional[str] = None,
        timeout_ms: int = 10000,
    ) -> list[Dict[str, Any]]:
        """Send multiple messages to Kafka topic.

        Args:
            messages: List of message dictionaries with 'value' and optional 'key'
            topic: Topic to send to (overrides default)
            timeout_ms: Timeout per message

        Returns:
            List of send results

        Raises:
            ProducerError: If batch send fails
        """
        if not messages:
            self.logger.warning("Empty message batch provided")
            return []

        results = []
        target_topic = topic or self.topic

        self.logger.info(f"Sending batch of {len(messages)} messages")

        for index, message in enumerate(messages):
            try:
                if not isinstance(message, dict):
                    raise ProducerError(
                        f"Message {index} must be dict, got {type(message)}"
                    )

                if "value" not in message:
                    raise ProducerError(f"Message {index} missing 'value' field")

                result = self.send_message(
                    value=message["value"],
                    key=message.get("key"),
                    topic=target_topic,
                    timeout_ms=timeout_ms,
                )
                results.append(result)

            except ProducerError as e:
                self.logger.error(f"Failed to send message {index}: {str(e)}")
                results.append({
                    "index": index,
                    "success": False,
                    "error": str(e),
                })

        self.logger.info(
            f"Batch send complete: {len([r for r in results if r.get('success')])} "
            f"successful, {len([r for r in results if not r.get('success')])} failed"
        )

        return results

    def flush(self, timeout_ms: int = 10000) -> None:
        """Flush pending messages.

        Args:
            timeout_ms: Timeout in milliseconds

        Raises:
            ProducerError: If flush fails
        """
        try:
            self.logger.debug("Flushing pending messages")
            self._producer.flush(timeout_secs=timeout_ms / 1000)
            self.logger.info("Messages flushed successfully")

        except LibKafkaError as e:
            error_msg = f"Failed to flush messages: {str(e)}"
            self.logger.error(error_msg)
            raise ProducerError(error_msg)

    def close(self) -> None:
        """Close producer connection."""
        try:
            self.logger.info("Closing KafkaProducer")
            if self._producer:
                self._producer.close()
                self._producer = None
            self.logger.info("KafkaProducer closed successfully")

        except Exception as e:
            self.logger.error(f"Error closing producer: {str(e)}")

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()

