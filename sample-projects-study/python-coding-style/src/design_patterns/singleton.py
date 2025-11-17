"""Singleton pattern implementation.

Ensures a class has only one instance and provides a global point of access.
"""

from typing import Dict, Any
import logging


# Method 1: Using decorator
def singleton(cls):
    """Decorator to create singleton from class.

    Args:
        cls: Class to make singleton

    Returns:
        Wrapped class with singleton behavior
    """
    instances: Dict[type, Any] = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Logger:
    """Singleton logger using decorator."""

    def __init__(self, name: str = "app"):
        """Initialize logger.

        Args:
            name: Logger name
        """
        self.name = name
        self._logger = logging.getLogger(name)

    def info(self, message: str):
        """Log info message.

        Args:
            message: Message to log
        """
        self._logger.info(message)


# Method 2: Using metaclass
class SingletonMeta(type):
    """Metaclass for singleton pattern."""

    _instances: Dict[type, Any] = {}

    def __call__(cls, *args, **kwargs):
        """Control instance creation.

        Args:
            *args: Positional arguments
            **kwargs: Keyword arguments

        Returns:
            Singleton instance
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DatabaseConnection(metaclass=SingletonMeta):
    """Singleton database connection using metaclass."""

    def __init__(self, connection_string: str = "localhost:5432"):
        """Initialize database connection.

        Args:
            connection_string: Connection string to database
        """
        self.connection_string = connection_string
        self.is_connected = False

    def connect(self) -> None:
        """Establish connection."""
        self.is_connected = True

    def disconnect(self) -> None:
        """Close connection."""
        self.is_connected = False

    def execute_query(self, query: str) -> Dict[str, Any]:
        """Execute database query.

        Args:
            query: SQL query

        Returns:
            Query result
        """
        if not self.is_connected:
            raise RuntimeError("Database not connected")
        return {"result": query}


# Method 3: Using class method (more Pythonic)
class Configuration:
    """Singleton configuration using class method."""

    _instance = None
    _config: Dict[str, Any] = {}

    def __new__(cls):
        """Control instance creation.

        Returns:
            Singleton instance
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def get_instance(cls):
        """Get singleton instance.

        Returns:
            Configuration instance
        """
        return cls()

    def set_config(self, key: str, value: Any) -> None:
        """Set configuration value.

        Args:
            key: Configuration key
            value: Configuration value
        """
        self._config[key] = value

    def get_config(self, key: str, default: Any = None) -> Any:
        """Get configuration value.

        Args:
            key: Configuration key
            default: Default value if not found

        Returns:
            Configuration value
        """
        return self._config.get(key, default)

    def get_all_config(self) -> Dict[str, Any]:
        """Get all configuration.

        Returns:
            All configuration settings
        """
        return self._config.copy()


# Method 4: Thread-safe singleton (for multi-threaded applications)
import threading


class ThreadSafeSingleton(type):
    """Thread-safe singleton metaclass."""

    _instances: Dict[type, Any] = {}
    _lock: threading.Lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        """Thread-safe instance creation.

        Args:
            *args: Positional arguments
            **kwargs: Keyword arguments

        Returns:
            Singleton instance
        """
        # Check without lock first (performance optimization)
        if cls not in cls._instances:
            # Acquire lock for actual creation
            with cls._lock:
                # Double-check pattern
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]


class CacheStore(metaclass=ThreadSafeSingleton):
    """Thread-safe singleton cache store."""

    def __init__(self):
        """Initialize cache store."""
        self._cache: Dict[str, Any] = {}
        self._lock = threading.Lock()

    def get(self, key: str) -> Any:
        """Get value from cache.

        Args:
            key: Cache key

        Returns:
            Cached value or None
        """
        with self._lock:
            return self._cache.get(key)

    def set(self, key: str, value: Any) -> None:
        """Set value in cache.

        Args:
            key: Cache key
            value: Value to cache
        """
        with self._lock:
            self._cache[key] = value

    def clear(self) -> None:
        """Clear all cache."""
        with self._lock:
            self._cache.clear()


# Usage examples and tests
if __name__ == "__main__":
    # Decorator approach
    logger1 = Logger("app")
    logger2 = Logger("other")
    assert logger1 is logger2  # Same instance

    # Metaclass approach
    db1 = DatabaseConnection()
    db1.connect()
    db2 = DatabaseConnection()
    assert db1 is db2  # Same instance
    assert db2.is_connected  # Same state

    # Class method approach
    config1 = Configuration.get_instance()
    config1.set_config("debug", True)
    config2 = Configuration.get_instance()
    assert config1 is config2  # Same instance
    assert config2.get_config("debug") is True  # Same data

    # Thread-safe approach
    cache1 = CacheStore()
    cache1.set("key", "value")
    cache2 = CacheStore()
    assert cache1 is cache2  # Same instance
    assert cache2.get("key") == "value"  # Same data

    print("✓ All singleton pattern examples work correctly")

