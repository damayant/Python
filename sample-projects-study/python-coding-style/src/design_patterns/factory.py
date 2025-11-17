"""Factory pattern implementations.

Provides an interface for creating objects in a superclass,
but lets subclasses decide which class to instantiate.
"""

from abc import ABC, abstractmethod
from typing import Dict, Type, Any


# Abstract base class
class DatabaseDriver(ABC):
    """Abstract base class for database drivers."""

    @abstractmethod
    def connect(self) -> bool:
        """Connect to database.

        Returns:
            True if connected
        """
        pass

    @abstractmethod
    def query(self, sql: str) -> list:
        """Execute query.

        Args:
            sql: SQL query

        Returns:
            Query results
        """
        pass

    @abstractmethod
    def close(self) -> None:
        """Close database connection."""
        pass


class MySQLDriver(DatabaseDriver):
    """MySQL database driver implementation."""

    def __init__(self, host: str = "localhost", port: int = 3306):
        """Initialize MySQL driver.

        Args:
            host: MySQL host
            port: MySQL port
        """
        self.host = host
        self.port = port
        self.connected = False

    def connect(self) -> bool:
        """Connect to MySQL database.

        Returns:
            True if connected
        """
        self.connected = True
        print(f"Connected to MySQL at {self.host}:{self.port}")
        return True

    def query(self, sql: str) -> list:
        """Execute MySQL query.

        Args:
            sql: SQL query

        Returns:
            Query results
        """
        if not self.connected:
            raise RuntimeError("Not connected to MySQL")
        return [{"result": f"MySQL: {sql}"}]

    def close(self) -> None:
        """Close MySQL connection."""
        self.connected = False
        print("MySQL connection closed")


class PostgreSQLDriver(DatabaseDriver):
    """PostgreSQL database driver implementation."""

    def __init__(self, host: str = "localhost", port: int = 5432):
        """Initialize PostgreSQL driver.

        Args:
            host: PostgreSQL host
            port: PostgreSQL port
        """
        self.host = host
        self.port = port
        self.connected = False

    def connect(self) -> bool:
        """Connect to PostgreSQL database.

        Returns:
            True if connected
        """
        self.connected = True
        print(f"Connected to PostgreSQL at {self.host}:{self.port}")
        return True

    def query(self, sql: str) -> list:
        """Execute PostgreSQL query.

        Args:
            sql: SQL query

        Returns:
            Query results
        """
        if not self.connected:
            raise RuntimeError("Not connected to PostgreSQL")
        return [{"result": f"PostgreSQL: {sql}"}]

    def close(self) -> None:
        """Close PostgreSQL connection."""
        self.connected = False
        print("PostgreSQL connection closed")


class SQLiteDriver(DatabaseDriver):
    """SQLite database driver implementation."""

    def __init__(self, database_file: str = ":memory:"):
        """Initialize SQLite driver.

        Args:
            database_file: Path to SQLite database file
        """
        self.database_file = database_file
        self.connected = False

    def connect(self) -> bool:
        """Connect to SQLite database.

        Returns:
            True if connected
        """
        self.connected = True
        print(f"Connected to SQLite: {self.database_file}")
        return True

    def query(self, sql: str) -> list:
        """Execute SQLite query.

        Args:
            sql: SQL query

        Returns:
            Query results
        """
        if not self.connected:
            raise RuntimeError("Not connected to SQLite")
        return [{"result": f"SQLite: {sql}"}]

    def close(self) -> None:
        """Close SQLite connection."""
        self.connected = False
        print("SQLite connection closed")


class DatabaseFactory:
    """Factory for creating database driver instances."""

    _drivers: Dict[str, Type[DatabaseDriver]] = {
        "mysql": MySQLDriver,
        "postgresql": PostgreSQLDriver,
        "sqlite": SQLiteDriver,
    }

    @classmethod
    def create_driver(
        cls,
        driver_type: str,
        **kwargs,
    ) -> DatabaseDriver:
        """Create database driver.

        Args:
            driver_type: Type of driver to create
            **kwargs: Arguments to pass to driver

        Returns:
            Database driver instance

        Raises:
            ValueError: If driver type is unknown
        """
        driver_type = driver_type.lower()

        if driver_type not in cls._drivers:
            raise ValueError(
                f"Unknown driver type: {driver_type}. "
                f"Available: {list(cls._drivers.keys())}"
            )

        driver_class = cls._drivers[driver_type]
        return driver_class(**kwargs)

    @classmethod
    def register_driver(
        cls,
        driver_type: str,
        driver_class: Type[DatabaseDriver],
    ) -> None:
        """Register a new driver type.

        Args:
            driver_type: Name of driver type
            driver_class: Driver class

        Raises:
            TypeError: If driver_class doesn't inherit DatabaseDriver
        """
        if not issubclass(driver_class, DatabaseDriver):
            raise TypeError(
                f"{driver_class.__name__} must inherit DatabaseDriver"
            )

        cls._drivers[driver_type.lower()] = driver_class

    @classmethod
    def get_available_drivers(cls) -> list:
        """Get list of available driver types.

        Returns:
            List of driver type names
        """
        return list(cls._drivers.keys())


# Alternative: Abstract Factory Pattern for complex object creation
class UIElement(ABC):
    """Abstract UI element."""

    @abstractmethod
    def render(self) -> str:
        """Render element.

        Returns:
            Rendered element string
        """
        pass


class WindowsButton(UIElement):
    """Windows button implementation."""

    def render(self) -> str:
        """Render Windows button.

        Returns:
            Rendered button string
        """
        return "Windows Button"


class MacButton(UIElement):
    """Mac button implementation."""

    def render(self) -> str:
        """Render Mac button.

        Returns:
            Rendered button string
        """
        return "Mac Button"


class UIFactory(ABC):
    """Abstract UI factory."""

    @abstractmethod
    def create_button(self) -> UIElement:
        """Create button.

        Returns:
            Button instance
        """
        pass


class WindowsUIFactory(UIFactory):
    """Windows UI factory."""

    def create_button(self) -> UIElement:
        """Create Windows button.

        Returns:
            Windows button instance
        """
        return WindowsButton()


class MacUIFactory(UIFactory):
    """Mac UI factory."""

    def create_button(self) -> UIElement:
        """Create Mac button.

        Returns:
            Mac button instance
        """
        return MacButton()


def create_ui_factory(platform: str) -> UIFactory:
    """Create appropriate UI factory for platform.

    Args:
        platform: Platform name ("windows" or "mac")

    Returns:
        UI factory instance

    Raises:
        ValueError: If platform is unknown
    """
    factories: Dict[str, UIFactory] = {
        "windows": WindowsUIFactory(),
        "mac": MacUIFactory(),
    }

    platform = platform.lower()
    if platform not in factories:
        raise ValueError(f"Unknown platform: {platform}")

    return factories[platform]


# Usage examples
if __name__ == "__main__":
    # Simple factory example
    print("=== Database Factory Example ===")
    print(f"Available drivers: {DatabaseFactory.get_available_drivers()}")

    mysql_db = DatabaseFactory.create_driver("mysql", host="db.example.com")
    mysql_db.connect()
    results = mysql_db.query("SELECT * FROM users")
    print(f"Results: {results}")
    mysql_db.close()

    sqlite_db = DatabaseFactory.create_driver("sqlite", database_file="app.db")
    sqlite_db.connect()
    sqlite_db.close()

    print("\n=== Abstract Factory Example ===")
    windows_factory = create_ui_factory("windows")
    button = windows_factory.create_button()
    print(f"Created: {button.render()}")

    mac_factory = create_ui_factory("mac")
    button = mac_factory.create_button()
    print(f"Created: {button.render()}")

