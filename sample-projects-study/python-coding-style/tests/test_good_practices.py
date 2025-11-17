"""Tests for good coding practices."""

import pytest
from src.good_practices.naming_conventions import (
    DatabaseConnection,
    DataProcessor,
    calculate_average_score,
    format_phone_number,
)
from src.good_practices.type_hints import (
    User,
    find_user_by_email,
    batch_process,
    Cache,
)
from src.good_practices.error_handling import (
    validate_email,
    safe_divide,
    ValidationError,
)
from src.good_practices.defensive_coding import (
    process_list_safely,
    get_nested_dict_value,
    calculate_percentage,
)


class TestNamingConventions:
    """Test naming conventions."""

    def test_database_connection(self):
        """Test database connection initialization."""
        db = DatabaseConnection("localhost:5432")
        assert db.connect() is True

    def test_data_processor(self):
        """Test data processor."""
        data = [
            {"id": 1, "status": "active"},
            {"id": 2, "status": "inactive"},
            {"id": 3, "status": "active"},
        ]
        processor = DataProcessor(data)
        active = processor.filter_by_status("active")
        assert len(active) == 2

    def test_calculate_average_score(self):
        """Test average score calculation."""
        scores = [90, 85, 95, 88]
        avg = calculate_average_score(scores)
        assert avg == 89.5

    def test_calculate_average_score_empty(self):
        """Test average with empty list."""
        with pytest.raises(ValueError):
            calculate_average_score([])

    def test_format_phone_number(self):
        """Test phone number formatting."""
        formatted = format_phone_number("1234567890")
        assert formatted == "(123) 456-7890"


class TestTypeHints:
    """Test type hints and annotations."""

    def test_user_model(self):
        """Test user data model."""
        from datetime import datetime
        user = User(
            user_id=1,
            username="john",
            email="john@example.com",
            created_at=datetime.now(),
        )
        assert user.user_id == 1
        assert user.username == "john"

    def test_find_user_by_email(self):
        """Test finding user by email."""
        from datetime import datetime
        users = [
            User(1, "alice", "alice@example.com", datetime.now()),
            User(2, "bob", "bob@example.com", datetime.now()),
        ]
        found = find_user_by_email("alice@example.com", users)
        assert found is not None
        assert found.username == "alice"

    def test_find_user_not_found(self):
        """Test finding non-existent user."""
        from datetime import datetime
        users = [
            User(1, "alice", "alice@example.com", datetime.now()),
        ]
        found = find_user_by_email("charlie@example.com", users)
        assert found is None

    def test_batch_process(self):
        """Test batch processing."""
        items = list(range(1, 11))
        batches = batch_process(items, batch_size=3)
        assert len(batches) == 4
        assert batches[0] == [1, 2, 3]
        assert batches[-1] == [10]

    def test_cache(self):
        """Test generic cache."""
        cache = Cache(max_size=2)
        cache.set("key1", "value1")
        cache.set("key2", "value2")
        assert cache.get("key1") == "value1"
        cache.set("key3", "value3")  # Should evict key1
        assert cache.get("key3") == "value3"


class TestErrorHandling:
    """Test error handling."""

    def test_validate_email_valid(self):
        """Test valid email validation."""
        assert validate_email("user@example.com") is True

    def test_validate_email_invalid(self):
        """Test invalid email validation."""
        with pytest.raises(ValidationError):
            validate_email("invalid-email")

    def test_validate_email_empty(self):
        """Test empty email validation."""
        with pytest.raises(ValidationError):
            validate_email("")

    def test_safe_divide_normal(self):
        """Test safe division."""
        result = safe_divide(10, 2)
        assert result == 5.0

    def test_safe_divide_by_zero(self):
        """Test division by zero."""
        result = safe_divide(10, 0, default_value=-1)
        assert result == -1

    def test_safe_divide_type_error(self):
        """Test type error handling."""
        result = safe_divide("a", "b", default_value=0)
        assert result == 0


class TestDefensiveCoding:
    """Test defensive coding practices."""

    def test_process_list_safely(self):
        """Test safe list processing."""
        result = process_list_safely([1, 2, 3], expected_type=int)
        assert result == [1, 2, 3]

    def test_process_list_invalid_type(self):
        """Test processing invalid list type."""
        with pytest.raises(TypeError):
            process_list_safely("not a list")

    def test_process_list_wrong_item_type(self):
        """Test processing with wrong item type."""
        with pytest.raises(TypeError):
            process_list_safely([1, "two", 3], expected_type=int)

    def test_get_nested_dict_value(self):
        """Test getting nested dictionary value."""
        data = {"user": {"name": "Alice", "age": 30}}
        value = get_nested_dict_value(data, ["user", "name"])
        assert value == "Alice"

    def test_get_nested_dict_value_missing(self):
        """Test getting missing nested value."""
        data = {"user": {"name": "Alice"}}
        value = get_nested_dict_value(data, ["user", "age"], default="Unknown")
        assert value == "Unknown"

    def test_calculate_percentage(self):
        """Test percentage calculation."""
        result = calculate_percentage(25, 100)
        assert result == 25.0

    def test_calculate_percentage_invalid(self):
        """Test invalid percentage calculation."""
        with pytest.raises(ValueError):
            calculate_percentage(-10, 100)

