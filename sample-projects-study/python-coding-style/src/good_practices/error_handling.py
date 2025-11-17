"""Proper error handling and exception practices.

Demonstrates defensive coding with appropriate exception handling.
"""

import logging
from typing import Optional, List, Any, Dict
from functools import wraps

logger = logging.getLogger(__name__)


class ValidationError(Exception):
    """Custom exception for validation errors."""

    pass


class ConfigurationError(Exception):
    """Custom exception for configuration errors."""

    pass


def validate_email(email: str) -> bool:
    """Validate email address with proper error handling.

    Args:
        email: Email address to validate

    Returns:
        True if valid email format

    Raises:
        ValidationError: If email is invalid
    """
    if not isinstance(email, str):
        raise ValidationError(f"Email must be string, got {type(email).__name__}")

    email = email.strip()

    if not email:
        raise ValidationError("Email cannot be empty")

    if "@" not in email or "." not in email.split("@")[-1]:
        raise ValidationError(f"Invalid email format: {email}")

    if len(email) > 254:
        raise ValidationError("Email is too long")

    return True


def safe_divide(
    numerator: float,
    denominator: float,
    default_value: float = 0.0,
) -> float:
    """Safely divide two numbers with specific exception handling.

    Args:
        numerator: Numerator
        denominator: Denominator
        default_value: Value to return on error

    Returns:
        Result of division or default value
    """
    try:
        if denominator == 0:
            logger.warning(f"Division by zero attempted: {numerator} / 0")
            return default_value

        result = numerator / denominator
        return result

    except TypeError as error:
        logger.error(f"Type error in division: {error}")
        return default_value
    except Exception as error:
        logger.error(f"Unexpected error in division: {error}")
        return default_value


def parse_json_safely(
    json_string: str,
    default_value: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Parse JSON with comprehensive error handling.

    Args:
        json_string: JSON string to parse
        default_value: Value to return on parse failure

    Returns:
        Parsed dictionary or default value
    """
    import json

    if default_value is None:
        default_value = {}

    if not isinstance(json_string, str):
        logger.warning(f"JSON input is not string: {type(json_string)}")
        return default_value

    if not json_string.strip():
        logger.warning("Empty JSON string provided")
        return default_value

    try:
        parsed = json.loads(json_string)
        return parsed if isinstance(parsed, dict) else default_value

    except json.JSONDecodeError as error:
        logger.error(f"JSON decode error: {error}")
        return default_value
    except Exception as error:
        logger.error(f"Unexpected error parsing JSON: {error}")
        return default_value


def retry_on_failure(
    max_attempts: int = 3,
    delay_seconds: float = 1.0,
    backoff_factor: float = 2.0,
):
    """Decorator to retry function on failure with exponential backoff.

    Args:
        max_attempts: Maximum number of attempts
        delay_seconds: Initial delay between attempts
        backoff_factor: Factor to increase delay by

    Returns:
        Decorated function
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            import time

            last_exception: Optional[Exception] = None
            current_delay = delay_seconds

            for attempt in range(1, max_attempts + 1):
                try:
                    logger.debug(
                        f"Attempt {attempt}/{max_attempts} for {func.__name__}"
                    )
                    return func(*args, **kwargs)

                except Exception as error:
                    last_exception = error
                    logger.warning(
                        f"Attempt {attempt} failed: {error}. "
                        f"Retrying in {current_delay}s..."
                    )

                    if attempt < max_attempts:
                        time.sleep(current_delay)
                        current_delay *= backoff_factor

            # All attempts failed
            error_msg = (
                f"Failed after {max_attempts} attempts: {last_exception}"
            )
            logger.error(error_msg)
            raise RuntimeError(error_msg) from last_exception

        return wrapper

    return decorator


def validate_config(config: Dict[str, Any]) -> None:
    """Validate configuration dictionary.

    Args:
        config: Configuration to validate

    Raises:
        ConfigurationError: If configuration is invalid
    """
    required_keys = ["database_url", "api_key", "log_level"]

    if not isinstance(config, dict):
        raise ConfigurationError(
            f"Configuration must be dict, got {type(config).__name__}"
        )

    missing_keys = [key for key in required_keys if key not in config]
    if missing_keys:
        raise ConfigurationError(
            f"Configuration missing required keys: {missing_keys}"
        )

    # Validate specific values
    valid_log_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    if config["log_level"] not in valid_log_levels:
        raise ConfigurationError(
            f"Invalid log_level: {config['log_level']}. "
            f"Must be one of {valid_log_levels}"
        )

    logger.info("Configuration validated successfully")


def handle_file_operation(
    filepath: str,
    operation: str = "read",
) -> Optional[str]:
    """Handle file operations with proper exception handling.

    Args:
        filepath: Path to file
        operation: Operation type ("read" or "write")

    Returns:
        File contents for read, None for write

    Raises:
        IOError: If file operation fails
    """
    try:
        if operation == "read":
            with open(filepath, "r") as file:
                contents = file.read()
            logger.info(f"Successfully read {len(contents)} bytes from {filepath}")
            return contents

        elif operation == "write":
            with open(filepath, "w") as file:
                file.write("Default content")
            logger.info(f"Successfully wrote to {filepath}")
            return None

        else:
            raise ValueError(f"Unknown operation: {operation}")

    except FileNotFoundError:
        error_msg = f"File not found: {filepath}"
        logger.error(error_msg)
        raise IOError(error_msg)

    except PermissionError:
        error_msg = f"Permission denied accessing {filepath}"
        logger.error(error_msg)
        raise IOError(error_msg)

    except IOError as error:
        logger.error(f"IO error: {error}")
        raise

    except Exception as error:
        error_msg = f"Unexpected error in file operation: {error}"
        logger.error(error_msg)
        raise IOError(error_msg)


class ResourceManager:
    """Demonstrate proper resource management with context managers."""

    def __init__(self, resource_name: str):
        """Initialize resource manager.

        Args:
            resource_name: Name of resource to manage
        """
        self.resource_name = resource_name
        self.is_open = False

    def __enter__(self):
        """Context manager entry - acquire resource."""
        try:
            logger.info(f"Acquiring resource: {self.resource_name}")
            self.is_open = True
            return self
        except Exception as error:
            logger.error(f"Failed to acquire resource: {error}")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - release resource."""
        try:
            logger.info(f"Releasing resource: {self.resource_name}")
            self.is_open = False

            if exc_type is not None:
                logger.error(
                    f"Exception during resource usage: {exc_type.__name__}: {exc_val}"
                )
            return False  # Don't suppress exceptions

        except Exception as error:
            logger.error(f"Error releasing resource: {error}")
            raise

    def use_resource(self) -> str:
        """Use the resource.

        Returns:
            Resource usage result

        Raises:
            RuntimeError: If resource not open
        """
        if not self.is_open:
            raise RuntimeError("Resource is not open")

        return f"Using {self.resource_name}"

