"""Defensive coding practices and techniques.

This module demonstrates defensive programming principles
to prevent bugs and unexpected behavior.
"""

from typing import List, Dict, Any, Optional, Union
from dataclasses import dataclass


@dataclass
class Person:
    """Person model with validation.

    Attributes:
        first_name: Person's first name
        last_name: Person's last name
        age: Person's age in years
    """

    first_name: str
    last_name: str
    age: int

    def __post_init__(self):
        """Validate fields after initialization.

        Raises:
            ValueError: If any field is invalid
        """
        if not isinstance(self.first_name, str) or not self.first_name.strip():
            raise ValueError("first_name must be non-empty string")

        if not isinstance(self.last_name, str) or not self.last_name.strip():
            raise ValueError("last_name must be non-empty string")

        if not isinstance(self.age, int) or self.age < 0 or self.age > 150:
            raise ValueError("age must be integer between 0 and 150")


def process_list_safely(
    items: Any,
    expected_type: Optional[type] = None,
) -> List[Any]:
    """Process list with defensive checks.

    Args:
        items: Items to process
        expected_type: Expected type of list items

    Returns:
        Validated and processed list

    Raises:
        TypeError: If input is not list or items have wrong type
    """
    # Check input type
    if not isinstance(items, list):
        raise TypeError(f"Expected list, got {type(items).__name__}")

    # Check for empty list
    if not items:
        return []

    # Validate item types if specified
    if expected_type is not None:
        invalid_items = [
            (idx, item) for idx, item in enumerate(items)
            if not isinstance(item, expected_type)
        ]

        if invalid_items:
            first_invalid_idx, first_invalid_item = invalid_items[0]
            raise TypeError(
                f"Item at index {first_invalid_idx} is {type(first_invalid_item).__name__}, "
                f"expected {expected_type.__name__}"
            )

    return items


def get_nested_dict_value(
    data: Any,
    keys: List[str],
    default: Any = None,
) -> Any:
    """Safely get value from nested dictionary.

    Args:
        data: Dictionary to search
        keys: List of keys to traverse
        default: Default value if key not found

    Returns:
        Value at nested path or default

    Raises:
        TypeError: If data is not dict or keys is not list
    """
    # Type checking
    if not isinstance(data, dict):
        raise TypeError(f"data must be dict, got {type(data).__name__}")

    if not isinstance(keys, list):
        raise TypeError(f"keys must be list, got {type(keys).__name__}")

    if not keys:
        raise ValueError("keys list cannot be empty")

    current = data

    for key in keys:
        # Validate key type
        if not isinstance(key, str):
            raise TypeError(f"Key must be string, got {type(key).__name__}")

        # Navigate nested structure
        if not isinstance(current, dict):
            return default

        current = current.get(key)

        if current is None:
            return default

    return current


def calculate_percentage(
    part: Union[int, float],
    total: Union[int, float],
    decimal_places: int = 2,
) -> float:
    """Calculate percentage with defensive checks.

    Args:
        part: Part value
        total: Total value
        decimal_places: Decimal places in result

    Returns:
        Percentage value

    Raises:
        TypeError: If values are not numeric
        ValueError: If values are invalid
    """
    # Type validation
    if not isinstance(part, (int, float)):
        raise TypeError(f"part must be numeric, got {type(part).__name__}")

    if not isinstance(total, (int, float)):
        raise TypeError(f"total must be numeric, got {type(total).__name__}")

    # Value validation
    if part < 0:
        raise ValueError("part cannot be negative")

    if total <= 0:
        raise ValueError("total must be positive")

    if part > total:
        raise ValueError("part cannot be greater than total")

    if not isinstance(decimal_places, int) or decimal_places < 0:
        raise ValueError("decimal_places must be non-negative integer")

    percentage = (part / total) * 100
    return round(percentage, decimal_places)


def merge_configs(
    base_config: Dict[str, Any],
    override_config: Dict[str, Any],
) -> Dict[str, Any]:
    """Merge configuration dictionaries defensively.

    Args:
        base_config: Base configuration
        override_config: Configuration to override with

    Returns:
        Merged configuration

    Raises:
        TypeError: If configs are not dictionaries
    """
    # Type checking
    if not isinstance(base_config, dict):
        raise TypeError(
            f"base_config must be dict, got {type(base_config).__name__}"
        )

    if not isinstance(override_config, dict):
        raise TypeError(
            f"override_config must be dict, got {type(override_config).__name__}"
        )

    # Deep copy to avoid modifying originals
    merged = dict(base_config)

    # Merge with defensive checks
    for key, value in override_config.items():
        # Validate key type
        if not isinstance(key, str):
            raise ValueError(f"Config key must be string, got {type(key).__name__}")

        # Nested dict merging
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = merge_configs(merged[key], value)
        else:
            merged[key] = value

    return merged


class BankAccount:
    """Bank account with defensive state management.

    Attributes:
        account_number: Unique account identifier
        balance: Current account balance
    """

    MIN_BALANCE = 0.0
    MAX_TRANSACTION = 1_000_000.0

    def __init__(self, account_number: str, initial_balance: float = 0.0):
        """Initialize account with validation.

        Args:
            account_number: Account number
            initial_balance: Initial balance

        Raises:
            ValueError: If parameters are invalid
        """
        if not isinstance(account_number, str) or not account_number.strip():
            raise ValueError("account_number must be non-empty string")

        if not isinstance(initial_balance, (int, float)):
            raise ValueError("initial_balance must be numeric")

        if initial_balance < self.MIN_BALANCE:
            raise ValueError(
                f"initial_balance cannot be less than {self.MIN_BALANCE}"
            )

        self._account_number = account_number
        self._balance = float(initial_balance)

    def deposit(self, amount: float) -> float:
        """Deposit money defensively.

        Args:
            amount: Amount to deposit

        Returns:
            New balance

        Raises:
            ValueError: If amount is invalid
        """
        if not isinstance(amount, (int, float)):
            raise ValueError(f"amount must be numeric, got {type(amount).__name__}")

        if amount <= 0:
            raise ValueError("amount must be positive")

        if amount > self.MAX_TRANSACTION:
            raise ValueError(f"amount exceeds maximum transaction {self.MAX_TRANSACTION}")

        self._balance += float(amount)
        return self._balance

    def withdraw(self, amount: float) -> float:
        """Withdraw money defensively.

        Args:
            amount: Amount to withdraw

        Returns:
            New balance

        Raises:
            ValueError: If amount is invalid or insufficient funds
        """
        if not isinstance(amount, (int, float)):
            raise ValueError(f"amount must be numeric, got {type(amount).__name__}")

        if amount <= 0:
            raise ValueError("amount must be positive")

        if amount > self.MAX_TRANSACTION:
            raise ValueError(f"amount exceeds maximum transaction {self.MAX_TRANSACTION}")

        if amount > self._balance:
            raise ValueError(
                f"insufficient funds: {amount} > {self._balance}"
            )

        self._balance -= float(amount)
        return self._balance

    def get_balance(self) -> float:
        """Get current balance safely.

        Returns:
            Current balance
        """
        return float(self._balance)

    def transfer(
        self,
        target_account: "BankAccount",
        amount: float,
    ) -> bool:
        """Transfer money to another account defensively.

        Args:
            target_account: Target account for transfer
            amount: Amount to transfer

        Returns:
            True if transfer successful

        Raises:
            ValueError: If transfer is invalid
            TypeError: If target_account is invalid
        """
        if not isinstance(target_account, BankAccount):
            raise TypeError(
                f"target_account must be BankAccount, "
                f"got {type(target_account).__name__}"
            )

        if target_account._account_number == self._account_number:
            raise ValueError("Cannot transfer to same account")

        # Perform transfer
        self.withdraw(amount)
        target_account.deposit(amount)
        return True

