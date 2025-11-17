"""Good naming conventions and practices.

This module demonstrates proper naming conventions following PEP 8
and Python best practices.
"""

from typing import List, Optional, Dict, Any
from enum import Enum


class UserRole(Enum):
    """Enumeration for user roles (UPPER_CASE for constants)."""

    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"


class DatabaseConnection:
    """Example class with proper naming (PascalCase for classes).

    Attributes:
        connection_string: The database connection string
        max_retries: Maximum number of connection retries
        is_connected: Whether currently connected
    """

    # Class constants in UPPER_CASE
    DEFAULT_TIMEOUT = 30
    MAX_POOL_SIZE = 10

    def __init__(self, connection_string: str, max_retries: int = 3):
        """Initialize database connection.

        Args:
            connection_string: Connection string to database
            max_retries: Maximum retries for connection
        """
        # Instance variables in snake_case
        self.connection_string = connection_string
        self.max_retries = max_retries
        self._is_connected = False
        self._connection = None

    def connect(self) -> bool:
        """Establish database connection.

        Returns:
            True if connection successful, False otherwise
        """
        # Implementation details
        self._is_connected = True
        return self._is_connected

    def _execute_query(self, query: str, params: Optional[List[Any]] = None) -> Dict:
        """Execute database query (private method with underscore prefix).

        Args:
            query: SQL query to execute
            params: Query parameters

        Returns:
            Query result as dictionary

        Raises:
            RuntimeError: If not connected
        """
        if not self._is_connected:
            raise RuntimeError("Not connected to database")

        # Implementation
        return {"result": "success"}

    def get_user_by_email(self, email_address: str) -> Optional[Dict[str, Any]]:
        """Retrieve user by email address (descriptive function name).

        Args:
            email_address: User email address

        Returns:
            User dictionary or None if not found
        """
        if not email_address or "@" not in email_address:
            return None

        query = "SELECT * FROM users WHERE email = ?"
        return self._execute_query(query, [email_address])

    def close(self) -> None:
        """Close database connection."""
        self._is_connected = False
        self._connection = None


class DataProcessor:
    """Process and transform data with clear naming."""

    def __init__(self, input_data: List[Dict[str, Any]]):
        """Initialize processor.

        Args:
            input_data: Data to process
        """
        self.input_data = input_data
        self.processed_data: List[Dict[str, Any]] = []
        self.error_count = 0

    def filter_by_status(
        self,
        status_value: str,
        inverse: bool = False
    ) -> List[Dict[str, Any]]:
        """Filter data by status field (clear parameter names).

        Args:
            status_value: Status to filter by
            inverse: If True, return items NOT matching status

        Returns:
            Filtered data list
        """
        filtered_items = [
            item for item in self.input_data
            if (item.get("status") == status_value) != inverse
        ]
        return filtered_items

    def transform_data(self) -> List[Dict[str, Any]]:
        """Transform all input data.

        Returns:
            Transformed data
        """
        self.processed_data = [
            self._transform_single_item(item)
            for item in self.input_data
        ]
        return self.processed_data

    def _transform_single_item(self, item: Dict[str, Any]) -> Dict[str, Any]:
        """Transform a single data item (private helper method).

        Args:
            item: Item to transform

        Returns:
            Transformed item
        """
        try:
            return {
                "id": item.get("id"),
                "name": item.get("name", "Unknown").upper(),
                "processed": True,
            }
        except (KeyError, AttributeError) as error:
            self.error_count += 1
            return {"error": str(error)}


# Function-level constants and configuration
DEFAULT_BATCH_SIZE = 100
CACHE_TTL_SECONDS = 3600


def calculate_average_score(scores: List[float]) -> float:
    """Calculate average score (clear, descriptive function name).

    Args:
        scores: List of scores

    Returns:
        Average score

    Raises:
        ValueError: If scores list is empty
    """
    if not scores:
        raise ValueError("Cannot calculate average of empty list")

    total_score = sum(scores)
    number_of_scores = len(scores)
    average_score = total_score / number_of_scores

    return average_score


def format_phone_number(phone_number_string: str) -> str:
    """Format phone number for display.

    Args:
        phone_number_string: Unformatted phone number

    Returns:
        Formatted phone number

    Example:
        >>> format_phone_number("1234567890")
        '(123) 456-7890'
    """
    # Remove non-digits
    digits_only = "".join(char for char in phone_number_string if char.isdigit())

    if len(digits_only) != 10:
        raise ValueError("Phone number must contain exactly 10 digits")

    formatted = f"({digits_only[:3]}) {digits_only[3:6]}-{digits_only[6:]}"
    return formatted

