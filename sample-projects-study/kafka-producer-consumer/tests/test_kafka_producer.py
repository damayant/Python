"""Tests for Kafka producer."""

import json
import pytest
from unittest.mock import Mock, MagicMock, patch

from src.kafka.producer import KafkaProducerService
from src.kafka.exceptions import ProducerError
from src.kafka.config import KafkaConfig


class TestKafkaProducerService:
    """Test cases for KafkaProducerService."""

    @pytest.fixture
    def mock_producer(self):
        """Create mock KafkaProducer."""
        return MagicMock()

    @pytest.fixture
    def config(self):
        """Create test configuration."""
        return KafkaConfig(
            bootstrap_servers=["localhost:9092"],
            topic="test-topic",
        )

    def test_initialization(self, config):
        """Test producer initialization."""
        with patch("src.kafka.producer.KafkaProducer"):
            producer = KafkaProducerService(config=config)
            assert producer.topic == "test-topic"
            assert producer.config == config

    def test_initialization_missing_topic(self):
        """Test initialization without topic."""
        config = KafkaConfig(topic=None)
        with pytest.raises(ProducerError):
            KafkaProducerService(config=config)

    def test_initialization_with_override_params(self):
        """Test initialization with override parameters."""
        config = KafkaConfig(topic="original-topic")
        with patch("src.kafka.producer.KafkaProducer"):
            producer = KafkaProducerService(
                config=config,
                topic="override-topic",
            )
            assert producer.topic == "override-topic"

    def test_serialize_key_none(self):
        """Test serializing None key."""
        result = KafkaProducerService._serialize_key(None)
        assert result is None

    def test_serialize_key_string(self):
        """Test serializing string key."""
        result = KafkaProducerService._serialize_key("test-key")
        assert result == b"test-key"

    def test_serialize_key_bytes(self):
        """Test serializing bytes key."""
        key = b"test-key"
        result = KafkaProducerService._serialize_key(key)
        assert result == key

    def test_serialize_key_dict(self):
        """Test serializing dict key."""
        key = {"id": 123}
        result = KafkaProducerService._serialize_key(key)
        assert result == json.dumps(key).encode("utf-8")

    def test_serialize_value_bytes(self):
        """Test serializing bytes value."""
        value = b"test-value"
        result = KafkaProducerService._serialize_value(value)
        assert result == value

    def test_serialize_value_string(self):
        """Test serializing string value."""
        value = "test-value"
        result = KafkaProducerService._serialize_value(value)
        assert result == b"test-value"

    def test_serialize_value_dict(self):
        """Test serializing dict value."""
        value = {"name": "test", "age": 30}
        result = KafkaProducerService._serialize_value(value)
        assert result == json.dumps(value).encode("utf-8")

    def test_serialize_value_invalid(self):
        """Test serializing invalid value type."""
        # This should work as it's convertible to JSON
        class NonSerializable:
            def __repr__(self):
                raise TypeError("Cannot serialize")

        with pytest.raises(ProducerError):
            obj = NonSerializable()
            KafkaProducerService._serialize_value(obj)

    def test_send_message_success(self, config):
        """Test successful message send."""
        with patch("src.kafka.producer.KafkaProducer") as mock_kafka:
            # Setup mock
            mock_future = MagicMock()
            mock_record_metadata = MagicMock()
            mock_record_metadata.topic = "test-topic"
            mock_record_metadata.partition = 0
            mock_record_metadata.offset = 100
            mock_record_metadata.timestamp = 1234567890

            mock_future.get.return_value = mock_record_metadata
            mock_kafka_instance = MagicMock()
            mock_kafka_instance.send.return_value = mock_future
            mock_kafka.return_value = mock_kafka_instance

            producer = KafkaProducerService(config=config)
            result = producer.send_message({"test": "data"})

            assert result["success"] is True
            assert result["topic"] == "test-topic"
            assert result["partition"] == 0
            assert result["offset"] == 100

    def test_send_message_with_key(self, config):
        """Test sending message with key."""
        with patch("src.kafka.producer.KafkaProducer") as mock_kafka:
            mock_future = MagicMock()
            mock_record_metadata = MagicMock()
            mock_record_metadata.topic = "test-topic"
            mock_record_metadata.partition = 0
            mock_record_metadata.offset = 100
            mock_record_metadata.timestamp = 1234567890

            mock_future.get.return_value = mock_record_metadata
            mock_kafka_instance = MagicMock()
            mock_kafka_instance.send.return_value = mock_future
            mock_kafka.return_value = mock_kafka_instance

            producer = KafkaProducerService(config=config)
            result = producer.send_message(
                value={"test": "data"},
                key="test-key",
            )

            assert result["success"] is True

    def test_send_message_missing_topic(self, config):
        """Test sending message without topic."""
        with patch("src.kafka.producer.KafkaProducer"):
            producer = KafkaProducerService(config=config)
            producer.topic = None
            with pytest.raises(ProducerError):
                producer.send_message({"test": "data"})

    def test_send_batch(self, config):
        """Test sending batch of messages."""
        with patch("src.kafka.producer.KafkaProducer") as mock_kafka:
            mock_future = MagicMock()
            mock_record_metadata = MagicMock()
            mock_record_metadata.topic = "test-topic"
            mock_record_metadata.partition = 0
            mock_record_metadata.offset = 100
            mock_record_metadata.timestamp = 1234567890

            mock_future.get.return_value = mock_record_metadata
            mock_kafka_instance = MagicMock()
            mock_kafka_instance.send.return_value = mock_future
            mock_kafka.return_value = mock_kafka_instance

            producer = KafkaProducerService(config=config)
            messages = [
                {"value": {"id": 1}},
                {"value": {"id": 2}, "key": "key2"},
                {"value": {"id": 3}},
            ]

            results = producer.send_batch(messages)

            assert len(results) == 3
            assert all(r["success"] for r in results)

    def test_send_batch_empty(self, config):
        """Test sending empty batch."""
        with patch("src.kafka.producer.KafkaProducer"):
            producer = KafkaProducerService(config=config)
            results = producer.send_batch([])
            assert results == []

    def test_send_batch_invalid_message(self, config):
        """Test sending batch with invalid message."""
        with patch("src.kafka.producer.KafkaProducer") as mock_kafka:
            mock_kafka_instance = MagicMock()
            mock_kafka.return_value = mock_kafka_instance

            producer = KafkaProducerService(config=config)
            messages = [
                {"value": {"id": 1}},
                "invalid",  # Not a dict
            ]

            results = producer.send_batch(messages)

            assert len(results) == 2
            assert results[0]["success"] is True
            assert results[1]["success"] is False

    def test_flush_success(self, config):
        """Test flushing pending messages."""
        with patch("src.kafka.producer.KafkaProducer") as mock_kafka:
            mock_kafka_instance = MagicMock()
            mock_kafka.return_value = mock_kafka_instance

            producer = KafkaProducerService(config=config)
            producer.flush()

            mock_kafka_instance.flush.assert_called_once()

    def test_close(self, config):
        """Test closing producer."""
        with patch("src.kafka.producer.KafkaProducer") as mock_kafka:
            mock_kafka_instance = MagicMock()
            mock_kafka.return_value = mock_kafka_instance

            producer = KafkaProducerService(config=config)
            producer.close()

            mock_kafka_instance.close.assert_called_once()

    def test_context_manager(self, config):
        """Test using producer as context manager."""
        with patch("src.kafka.producer.KafkaProducer") as mock_kafka:
            mock_kafka_instance = MagicMock()
            mock_kafka.return_value = mock_kafka_instance

            with KafkaProducerService(config=config) as producer:
                assert producer is not None

            mock_kafka_instance.close.assert_called_once()

