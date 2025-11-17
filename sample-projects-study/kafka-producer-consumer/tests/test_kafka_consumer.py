"""Tests for Kafka consumer."""

import pytest
from unittest.mock import Mock, MagicMock, patch

from src.kafka.consumer import KafkaConsumerService
from src.kafka.exceptions import ConsumerError
from src.kafka.config import KafkaConfig


class TestKafkaConsumerService:
    """Test cases for KafkaConsumerService."""

    @pytest.fixture
    def config(self):
        """Create test configuration."""
        return KafkaConfig(
            bootstrap_servers=["localhost:9092"],
            topic="test-topic",
            group_id="test-group",
        )

    def test_initialization(self, config):
        """Test consumer initialization."""
        with patch("src.kafka.consumer.KafkaConsumer"):
            consumer = KafkaConsumerService(config=config)
            assert consumer.topic == "test-topic"
            assert consumer.group_id == "test-group"

    def test_initialization_missing_topic(self):
        """Test initialization without topic."""
        config = KafkaConfig(
            bootstrap_servers=["localhost:9092"],
            topic=None,
            group_id="test-group",
        )
        with pytest.raises(ConsumerError):
            KafkaConsumerService(config=config)

    def test_initialization_missing_group_id(self):
        """Test initialization without group_id."""
        config = KafkaConfig(
            bootstrap_servers=["localhost:9092"],
            topic="test-topic",
            group_id=None,
        )
        with pytest.raises(ConsumerError):
            KafkaConsumerService(config=config)

    def test_initialization_with_override_params(self, config):
        """Test initialization with override parameters."""
        with patch("src.kafka.consumer.KafkaConsumer"):
            consumer = KafkaConsumerService(
                config=config,
                topic="override-topic",
                group_id="override-group",
            )
            assert consumer.topic == "override-topic"
            assert consumer.group_id == "override-group"

    def test_deserialize_key_none(self):
        """Test deserializing None key."""
        result = KafkaConsumerService._deserialize_key(None)
        assert result is None

    def test_deserialize_key_bytes(self):
        """Test deserializing bytes key."""
        result = KafkaConsumerService._deserialize_key(b"test-key")
        assert result == "test-key"

    def test_deserialize_key_non_utf8(self):
        """Test deserializing non-UTF8 bytes key."""
        result = KafkaConsumerService._deserialize_key(b"\xff\xfe")
        # Should return raw bytes
        assert isinstance(result, bytes)

    def test_deserialize_value_none(self):
        """Test deserializing None value."""
        result = KafkaConsumerService._deserialize_value(None)
        assert result is None

    def test_deserialize_value_string(self):
        """Test deserializing string value."""
        result = KafkaConsumerService._deserialize_value(b"test-value")
        assert result == "test-value"

    def test_deserialize_value_json(self):
        """Test deserializing JSON value."""
        import json
        data = {"name": "test", "age": 30}
        result = KafkaConsumerService._deserialize_value(json.dumps(data).encode())
        assert result == data

    def test_deserialize_value_invalid_utf8(self):
        """Test deserializing invalid UTF-8 value."""
        with pytest.raises(ConsumerError):
            KafkaConsumerService._deserialize_value(b"\xff\xfe")

    def test_consume(self, config):
        """Test consuming messages."""
        with patch("src.kafka.consumer.KafkaConsumer") as mock_kafka:
            mock_kafka_instance = MagicMock()

            # Create mock messages
            from collections import namedtuple
            ConsumerRecord = namedtuple(
                "ConsumerRecord",
                ["topic", "partition", "offset", "timestamp", "key", "value", "headers"]
            )

            record = ConsumerRecord(
                topic="test-topic",
                partition=0,
                offset=0,
                timestamp=1234567890,
                key=b"key1",
                value=b'{"data": "value"}',
                headers=[],
            )

            from kafka import TopicPartition
            tp = TopicPartition("test-topic", 0)
            mock_kafka_instance.poll.side_effect = [
                {tp: [record]},  # First call returns message
                {},  # Second call returns empty
            ]

            mock_kafka.return_value = mock_kafka_instance

            consumer = KafkaConsumerService(config=config)
            messages = list(consumer.consume(timeout_ms=100, max_messages=1))

            assert len(messages) == 1
            assert messages[0]["topic"] == "test-topic"
            assert messages[0]["offset"] == 0

    def test_seek_to_beginning(self, config):
        """Test seeking to beginning."""
        with patch("src.kafka.consumer.KafkaConsumer") as mock_kafka:
            mock_kafka_instance = MagicMock()
            mock_kafka.return_value = mock_kafka_instance

            consumer = KafkaConsumerService(config=config)
            consumer.seek_to_beginning()

            mock_kafka_instance.seek_to_beginning.assert_called_once()

    def test_seek_to_end(self, config):
        """Test seeking to end."""
        with patch("src.kafka.consumer.KafkaConsumer") as mock_kafka:
            mock_kafka_instance = MagicMock()
            mock_kafka.return_value = mock_kafka_instance

            consumer = KafkaConsumerService(config=config)
            consumer.seek_to_end()

            mock_kafka_instance.seek_to_end.assert_called_once()

    def test_commit(self, config):
        """Test committing offset."""
        with patch("src.kafka.consumer.KafkaConsumer") as mock_kafka:
            mock_kafka_instance = MagicMock()
            mock_kafka.return_value = mock_kafka_instance

            consumer = KafkaConsumerService(config=config)
            consumer.commit()

            mock_kafka_instance.commit.assert_called_once()

    def test_close(self, config):
        """Test closing consumer."""
        with patch("src.kafka.consumer.KafkaConsumer") as mock_kafka:
            mock_kafka_instance = MagicMock()
            mock_kafka.return_value = mock_kafka_instance

            consumer = KafkaConsumerService(config=config)
            consumer.close()

            mock_kafka_instance.close.assert_called_once()

    def test_context_manager(self, config):
        """Test using consumer as context manager."""
        with patch("src.kafka.consumer.KafkaConsumer") as mock_kafka:
            mock_kafka_instance = MagicMock()
            mock_kafka.return_value = mock_kafka_instance

            with KafkaConsumerService(config=config) as consumer:
                assert consumer is not None

            mock_kafka_instance.close.assert_called_once()

