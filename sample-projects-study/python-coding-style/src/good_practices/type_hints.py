"""Type hints and annotations - good practices.

This module demonstrates proper use of type hints in Python
for improved code clarity and IDE support.
"""

from typing import List, Dict, Optional, Union, Tuple, Callable, Any, TypeVar, Generic
from dataclasses import dataclass
from datetime import datetime


# Type variables for generic functions
T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


@dataclass
class User:
    """User data model with type hints.

    Attributes:
        user_id: Unique user identifier
        username: User's login name
        email: User's email address
        created_at: When user account was created
        is_active: Whether user account is active
    """

    user_id: int
    username: str
    email: str
    created_at: datetime
    is_active: bool = True


def process_user_data(
    user_ids: List[int],
    user_names: Dict[int, str],
) -> Dict[int, User]:
    """Process multiple users with type hints for collections.

    Args:
        user_ids: List of user IDs to process
        user_names: Mapping of user ID to username

    Returns:
        Dictionary mapping user ID to User objects
    """
    users: Dict[int, User] = {}

    for user_id in user_ids:
        if user_id in user_names:
            user = User(
                user_id=user_id,
                username=user_names[user_id],
                email=f"{user_names[user_id]}@example.com",
                created_at=datetime.now(),
            )
            users[user_id] = user

    return users


def find_user_by_email(
    email: str,
    users: List[User],
) -> Optional[User]:
    """Find user by email with Optional type hint.

    Args:
        email: Email to search for
        users: List of users

    Returns:
        User if found, None otherwise
    """
    for user in users:
        if user.email == email:
            return user

    return None


def convert_value(
    value: Any,
    target_type: type,
) -> Union[int, str, float, None]:
    """Convert value to target type with Union type hint.

    Args:
        value: Value to convert
        target_type: Target type class

    Returns:
        Converted value or None if conversion fails
    """
    try:
        if target_type == int:
            return int(value)
        elif target_type == str:
            return str(value)
        elif target_type == float:
            return float(value)
    except (ValueError, TypeError):
        return None

    return None


def batch_process(
    items: List[T],
    batch_size: int = 100,
) -> List[List[T]]:
    """Process items in batches using generic type.

    Args:
        items: Items to batch
        batch_size: Size of each batch

    Returns:
        List of batches
    """
    batches: List[List[T]] = []

    for start_index in range(0, len(items), batch_size):
        end_index = min(start_index + batch_size, len(items))
        batch = items[start_index:end_index]
        batches.append(batch)

    return batches


def apply_to_dict(
    data: Dict[K, V],
    transform_func: Callable[[V], V],
) -> Dict[K, V]:
    """Apply transformation function to dictionary values.

    Args:
        data: Dictionary to transform
        transform_func: Function to apply to values

    Returns:
        Dictionary with transformed values
    """
    transformed: Dict[K, V] = {}

    for key, value in data.items():
        try:
            transformed[key] = transform_func(value)
        except Exception:
            transformed[key] = value

    return transformed


def get_nested_value(
    data: Dict[str, Any],
    keys: List[str],
    default_value: Any = None,
) -> Any:
    """Safely get nested dictionary value with type hints.

    Args:
        data: Dictionary to search
        keys: List of keys to traverse
        default_value: Value to return if key not found

    Returns:
        Value at nested key or default
    """
    current_value: Any = data

    for key in keys:
        if isinstance(current_value, dict):
            current_value = current_value.get(key)
            if current_value is None:
                return default_value
        else:
            return default_value

    return current_value


class Cache(Generic[T]):
    """Generic cache class with type hints.

    Attributes:
        data: Cached data storage
        max_size: Maximum number of items
    """

    def __init__(self, max_size: int = 100):
        """Initialize cache.

        Args:
            max_size: Maximum items to store
        """
        self.data: Dict[str, T] = {}
        self.max_size: int = max_size

    def get(self, key: str) -> Optional[T]:
        """Get cached value.

        Args:
            key: Cache key

        Returns:
            Cached value or None
        """
        return self.data.get(key)

    def set(self, key: str, value: T) -> None:
        """Set cache value.

        Args:
            key: Cache key
            value: Value to cache
        """
        if len(self.data) >= self.max_size:
            # Remove oldest item (simplified)
            first_key = next(iter(self.data))
            del self.data[first_key]

        self.data[key] = value

    def clear(self) -> None:
        """Clear all cache."""
        self.data.clear()


def calculate_statistics(
    values: List[float],
) -> Tuple[float, float, float]:
    """Calculate min, max, average with tuple return type.

    Args:
        values: List of numeric values

    Returns:
        Tuple of (min_value, max_value, average_value)

    Raises:
        ValueError: If values list is empty
    """
    if not values:
        raise ValueError("Cannot calculate statistics for empty list")

    min_value: float = min(values)
    max_value: float = max(values)
    average_value: float = sum(values) / len(values)

    return min_value, max_value, average_value


def merge_dicts(
    *dicts: Dict[str, Any],
    deep_merge: bool = False,
) -> Dict[str, Any]:
    """Merge multiple dictionaries with type hints.

    Args:
        *dicts: Variable number of dictionaries
        deep_merge: Whether to merge nested dictionaries

    Returns:
        Merged dictionary
    """
    result: Dict[str, Any] = {}

    for current_dict in dicts:
        for key, value in current_dict.items():
            if deep_merge and key in result and isinstance(result[key], dict):
                result[key].update(value)
            else:
                result[key] = value

    return result

