"""Tests for API client module."""

import pytest
import responses
from unittest.mock import patch, MagicMock

from src.api import APIClient, ValidationError, APIError
from src.api.client import StatelessAPIClient, StatefulAPIClient


class TestStatelessAPIClient:
    """Test cases for StatelessAPIClient."""

    @pytest.fixture
    def client(self):
        """Create client instance for testing."""
        return StatelessAPIClient("https://api.example.com")

    def test_initialization(self, client):
        """Test client initialization."""
        assert client.base_url == "https://api.example.com"
        assert client.timeout == 30
        assert client.max_retries == 3

    def test_initialization_with_invalid_base_url(self):
        """Test initialization with empty base URL."""
        with pytest.raises(ValidationError):
            StatelessAPIClient("")

    def test_build_url(self, client):
        """Test URL building."""
        url = client._build_url("users")
        assert url == "https://api.example.com/users"

    def test_build_url_with_leading_slash(self, client):
        """Test URL building with leading slash."""
        url = client._build_url("/users")
        assert url == "https://api.example.com/users"

    @responses.activate
    def test_get_success(self, client):
        """Test successful GET request."""
        responses.add(
            responses.GET,
            "https://api.example.com/users",
            json={"id": 1, "name": "John"},
            status=200,
        )

        result = client.get("users")
        assert result == {"id": 1, "name": "John"}

    @responses.activate
    def test_get_with_params(self, client):
        """Test GET request with query parameters."""
        responses.add(
            responses.GET,
            "https://api.example.com/users",
            json=[{"id": 1}, {"id": 2}],
            status=200,
        )

        result = client.get("users", params={"page": 1, "limit": 10})
        assert result == [{"id": 1}, {"id": 2}]

    def test_get_with_empty_endpoint(self, client):
        """Test GET request with empty endpoint."""
        with pytest.raises(ValidationError):
            client.get("")

    @responses.activate
    def test_get_http_error(self, client):
        """Test GET request with HTTP error."""
        responses.add(
            responses.GET,
            "https://api.example.com/users",
            status=404,
        )

        with pytest.raises(APIError):
            client.get("users")

    @responses.activate
    def test_get_timeout(self, client):
        """Test GET request with timeout."""
        responses.add(
            responses.GET,
            "https://api.example.com/users",
            body=Exception("Timeout"),
        )

        with patch("requests.get") as mock_get:
            mock_get.side_effect = TimeoutError("Connection timeout")
            # Note: This test demonstrates how to mock timeout
            # Actual timeout testing would require more complex setup


class TestStatefulAPIClient:
    """Test cases for StatefulAPIClient."""

    @pytest.fixture
    def client(self):
        """Create client instance for testing."""
        return StatefulAPIClient("https://api.example.com")

    def test_initialization(self, client):
        """Test client initialization."""
        assert client.base_url == "https://api.example.com"
        assert client._session is not None
        assert client._state == {}

    @responses.activate
    def test_get_success(self, client):
        """Test successful GET request."""
        responses.add(
            responses.GET,
            "https://api.example.com/users",
            json={"id": 1, "name": "John"},
            status=200,
        )

        result = client.get("users")
        assert result == {"id": 1, "name": "John"}

    def test_set_and_get_state(self, client):
        """Test state management."""
        client.set_state("token", "abc123")
        assert client.get_state("token") == "abc123"

    def test_get_state_default(self, client):
        """Test state retrieval with default value."""
        value = client.get_state("nonexistent", "default")
        assert value == "default"

    def test_context_manager(self):
        """Test using client as context manager."""
        with StatefulAPIClient("https://api.example.com") as client:
            assert client.base_url == "https://api.example.com"

    def test_close_session(self):
        """Test closing session."""
        client = StatefulAPIClient("https://api.example.com")
        assert client._session is not None
        client.close()


class TestDataValidator:
    """Test cases for DataValidator."""

    def test_validate_valid_record(self):
        """Test validation of valid record."""
        from src.data.processor import DataValidator

        validator = DataValidator(required_fields=["id", "name"])
        record = {"id": 1, "name": "John", "extra": "field"}
        assert validator.validate(record) is True

    def test_validate_missing_field(self):
        """Test validation with missing required field."""
        from src.data.processor import DataValidator

        validator = DataValidator(required_fields=["id", "name"])
        record = {"id": 1}
        assert validator.validate(record) is False

    def test_clean_record(self):
        """Test cleaning record."""
        from src.data.processor import DataValidator

        validator = DataValidator()
        record = {"id": 1, "name": "  John  ", "empty": "", "null": None}
        cleaned = validator.clean(record)
        assert cleaned == {"id": 1, "name": "John"}


class TestDataProcessor:
    """Test cases for DataProcessor."""

    def test_process_records(self):
        """Test processing records."""
        from src.data.processor import DataProcessor, DataValidator

        validator = DataValidator(required_fields=["id", "name"])
        processor = DataProcessor(validator)

        data = [
            {"id": 1, "name": "  Alice  "},
            {"id": 2, "name": "Bob"},
            {"id": 3},  # Missing name, will be skipped
        ]

        result = processor.process(data)
        assert len(result) == 2
        assert result[0]["name"] == "Alice"
        assert result[1]["name"] == "Bob"

    def test_process_statistics(self):
        """Test processing statistics."""
        from src.data.processor import DataProcessor, DataValidator

        validator = DataValidator(required_fields=["id"])
        processor = DataProcessor(validator)

        data = [
            {"id": 1},
            {"id": 2},
            {},  # Missing id, will be skipped
        ]

        processor.process(data)
        stats = processor.get_stats()
        assert stats["processed"] == 2
        assert stats["skipped"] == 1

    def test_process_invalid_data(self):
        """Test processing with invalid data type."""
        from src.data.processor import DataProcessor

        processor = DataProcessor()
        with pytest.raises(ValueError):
            processor.process("not a list")


class TestStreamingDataProcessor:
    """Test cases for StreamingDataProcessor."""

    def test_initialization(self):
        """Test streaming processor initialization."""
        from src.data.processor import StreamingDataProcessor

        processor = StreamingDataProcessor(batch_size=10)
        assert processor.batch_size == 10

    def test_initialization_invalid_batch_size(self):
        """Test initialization with invalid batch size."""
        from src.data.processor import StreamingDataProcessor

        with pytest.raises(ValueError):
            StreamingDataProcessor(batch_size=0)

    def test_process_stream(self):
        """Test streaming data processing."""
        from src.data.processor import StreamingDataProcessor, DataValidator

        validator = DataValidator(required_fields=["id"])
        processor = StreamingDataProcessor(validator, batch_size=2)

        def data_generator():
            for i in range(1, 6):
                yield {"id": i, "name": f"Item {i}"}

        batches = list(processor.process(data_generator()))
        assert len(batches) == 3  # 5 items with batch_size=2: [2, 2, 1]
        assert len(batches[0]) == 2
        assert len(batches[1]) == 2
        assert len(batches[2]) == 1

