"""Kafka consumer implementation."""

import json
import logging
from typing import Any, Dict, Generator, Optional

from kafka import KafkaConsumer, TopicPartition
from kafka.errors import KafkaError as LibKafkaError

from .config import KafkaConfig
from .exceptions import ConsumerError


class KafkaConsumerService:
    """Service for consuming messages from Kafka topics."""

    def __init__(
        self,
        config: Optional[KafkaConfig] = None,
        bootstrap_servers: Optional[list] = None,
        topic: Optional[str] = None,
        group_id: Optional[str] = None,
    ):
        """Initialize Kafka consumer service.

        Args:
            config: KafkaConfig instance
            bootstrap_servers: List of bootstrap servers (overrides config)
            topic: Kafka topic (overrides config)
            group_id: Consumer group ID (overrides config)

        Raises:
            ConsumerError: If initialization fails
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
        if group_id:
            config.group_id = group_id

        self.config = config
        self.topic = config.topic
        self.group_id = config.group_id

        if not self.topic:
            raise ConsumerError("Topic must be specified")

        if not self.group_id:
            raise ConsumerError("Consumer group_id must be specified")

        self._consumer = self._create_consumer()
        self.logger.info(
            f"KafkaConsumerService initialized for topic: {self.topic}, "
            f"group: {self.group_id}"
        )

    def _create_consumer(self) -> KafkaConsumer:
        """Create Kafka consumer instance.

        Returns:
            KafkaConsumer instance

        Raises:
            ConsumerError: If consumer creation fails
        """
        try:
            consumer = KafkaConsumer(
                self.topic,
                bootstrap_servers=self.config.bootstrap_servers,
                group_id=self.group_id,
                client_id=self.config.client_id,
                auto_offset_reset=self.config.auto_offset_reset,
                enable_auto_commit=self.config.enable_auto_commit,
                max_poll_records=self.config.max_poll_records,
                session_timeout_ms=self.config.session_timeout_ms,
                request_timeout_ms=self.config.request_timeout_ms,
                value_deserializer=self._deserialize_value,
                key_deserializer=self._deserialize_key,
            )
            self.logger.debug("KafkaConsumer instance created successfully")
            return consumer

        except LibKafkaError as e:
            error_msg = f"Failed to create KafkaConsumer: {str(e)}"
            self.logger.error(error_msg)
            raise ConsumerError(error_msg)

    @staticmethod
    def _deserialize_key(key: Optional[bytes]) -> Optional[Any]:
        """Deserialize message key.

        Args:
            key: Serialized key bytes

        Returns:
            Deserialized key
        """
        if key is None:
            return None

        try:
            # Try to decode as string first
            return key.decode("utf-8")
        except UnicodeDecodeError:
            # If not UTF-8, return raw bytes
            return key

    @staticmethod
    def _deserialize_value(value: bytes) -> Any:
        """Deserialize message value.

        Args:
            value: Serialized value bytes

        Returns:
            Deserialized value

        Raises:
            ConsumerError: If deserialization fails
        """
        if value is None:
            return None

        try:
            # Decode bytes to string
            value_str = value.decode("utf-8")

            # Try to parse as JSON
            try:
                return json.loads(value_str)
            except json.JSONDecodeError:
                # If not JSON, return as string
                return value_str

        except UnicodeDecodeError as e:
            raise ConsumerError(f"Failed to deserialize value: {str(e)}")

    def consume(
        self,
        timeout_ms: int = 1000,
        max_messages: Optional[int] = None,
    ) -> Generator[Dict[str, Any], None, None]:
        """Consume messages from topic.

        Args:
            timeout_ms: Poll timeout in milliseconds
            max_messages: Maximum messages to consume (None for infinite)

        Yields:
            Message dictionaries with metadata

        Raises:
            ConsumerError: If consumption fails
        """
        message_count = 0

        try:
            self.logger.info(
                f"Starting to consume from topic: {self.topic}, "
                f"timeout: {timeout_ms}ms"
            )

            while True:
                # Check if we've reached max messages
                if max_messages and message_count >= max_messages:
                    self.logger.info(f"Reached max messages limit: {max_messages}")
                    break

                try:
                    # Poll for messages
                    messages = self._consumer.poll(timeout_ms=timeout_ms)

                    if not messages:
                        self.logger.debug("No messages received in poll")
                        continue

                    # Process each partition
                    for topic_partition, records in messages.items():
                        for record in records:
                            message_dict = {
                                "topic": record.topic,
                                "partition": record.partition,
                                "offset": record.offset,
                                "timestamp": record.timestamp,
                                "key": record.key,
                                "value": record.value,
                                "headers": record.headers or [],
                            }

                            self.logger.debug(
                                f"Received message from {record.topic}:"
                                f"{record.partition}:{record.offset}"
                            )

                            message_count += 1
                            yield message_dict

                except LibKafkaError as e:
                    error_msg = f"Error during consumption: {str(e)}"
                    self.logger.error(error_msg)
                    raise ConsumerError(error_msg)

        except GeneratorExit:
            self.logger.info(f"Consumer stopped, received {message_count} messages")
        except ConsumerError:
            raise
        except Exception as e:
            error_msg = f"Unexpected error during consumption: {str(e)}"
            self.logger.error(error_msg)
            raise ConsumerError(error_msg)

    def seek_to_beginning(self) -> None:
        """Seek to beginning of all partitions.

        Raises:
            ConsumerError: If seek fails
        """
        try:
            self.logger.info("Seeking to beginning of all partitions")
            self._consumer.seek_to_beginning()
            self.logger.info("Successfully seeked to beginning")

        except LibKafkaError as e:
            error_msg = f"Failed to seek to beginning: {str(e)}"
            self.logger.error(error_msg)
            raise ConsumerError(error_msg)

    def seek_to_end(self) -> None:
        """Seek to end of all partitions.

        Raises:
            ConsumerError: If seek fails
        """
        try:
            self.logger.info("Seeking to end of all partitions")
            self._consumer.seek_to_end()
            self.logger.info("Successfully seeked to end")

        except LibKafkaError as e:
            error_msg = f"Failed to seek to end: {str(e)}"
            self.logger.error(error_msg)
            raise ConsumerError(error_msg)

    def commit(self) -> None:
        """Commit current offset.

        Raises:
            ConsumerError: If commit fails
        """
        try:
            self.logger.debug("Committing current offset")
            self._consumer.commit()
            self.logger.info("Offset committed successfully")

        except LibKafkaError as e:
            error_msg = f"Failed to commit offset: {str(e)}"
            self.logger.error(error_msg)
            raise ConsumerError(error_msg)

    def close(self) -> None:
        """Close consumer connection."""
        try:
            self.logger.info("Closing KafkaConsumer")
            if self._consumer:
                self._consumer.close()
                self._consumer = None
            self.logger.info("KafkaConsumer closed successfully")

        except Exception as e:
            self.logger.error(f"Error closing consumer: {str(e)}")

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()

