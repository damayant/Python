"""Tests for design patterns."""

import pytest
from src.design_patterns.singleton import (
    Logger,
    DatabaseConnection,
    Configuration,
    CacheStore,
)
from src.design_patterns.factory import (
    DatabaseFactory,
    create_ui_factory,
)


class TestSingletonPattern:
    """Test singleton pattern implementations."""

    def test_logger_singleton(self):
        """Test logger singleton."""
        logger1 = Logger()
        logger2 = Logger()
        assert logger1 is logger2

    def test_database_connection_singleton(self):
        """Test database connection singleton."""
        db1 = DatabaseConnection("localhost:5432")
        db2 = DatabaseConnection("different:9999")
        assert db1 is db2
        assert db1.connection_string == "localhost:5432"

    def test_database_connection_state_shared(self):
        """Test that singleton shares state."""
        db1 = DatabaseConnection()
        db1.connect()
        db2 = DatabaseConnection()
        assert db2.is_connected is True

    def test_configuration_singleton(self):
        """Test configuration singleton."""
        config1 = Configuration.get_instance()
        config1.set_config("debug", True)
        config2 = Configuration.get_instance()
        assert config1 is config2
        assert config2.get_config("debug") is True

    def test_cache_store_singleton(self):
        """Test thread-safe cache store singleton."""
        cache1 = CacheStore()
        cache1.set("key", "value")
        cache2 = CacheStore()
        assert cache1 is cache2
        assert cache2.get("key") == "value"


class TestFactoryPattern:
    """Test factory pattern implementations."""

    def test_create_mysql_driver(self):
        """Test creating MySQL driver."""
        driver = DatabaseFactory.create_driver("mysql")
        assert driver is not None
        assert driver.connect() is True

    def test_create_postgresql_driver(self):
        """Test creating PostgreSQL driver."""
        driver = DatabaseFactory.create_driver("postgresql")
        assert driver is not None
        assert driver.connect() is True

    def test_create_sqlite_driver(self):
        """Test creating SQLite driver."""
        driver = DatabaseFactory.create_driver("sqlite", database_file=":memory:")
        assert driver is not None
        assert driver.connect() is True

    def test_factory_unknown_driver(self):
        """Test factory with unknown driver type."""
        with pytest.raises(ValueError):
            DatabaseFactory.create_driver("mongodb")

    def test_factory_case_insensitive(self):
        """Test factory is case insensitive."""
        driver1 = DatabaseFactory.create_driver("MySQL")
        driver2 = DatabaseFactory.create_driver("mysql")
        # Should be same driver type
        assert type(driver1).__name__ == type(driver2).__name__

    def test_get_available_drivers(self):
        """Test getting list of available drivers."""
        drivers = DatabaseFactory.get_available_drivers()
        assert "mysql" in drivers
        assert "postgresql" in drivers
        assert "sqlite" in drivers

    def test_ui_factory_windows(self):
        """Test Windows UI factory."""
        factory = create_ui_factory("windows")
        button = factory.create_button()
        assert button.render() == "Windows Button"

    def test_ui_factory_mac(self):
        """Test Mac UI factory."""
        factory = create_ui_factory("mac")
        button = factory.create_button()
        assert button.render() == "Mac Button"

    def test_ui_factory_unknown_platform(self):
        """Test UI factory with unknown platform."""
        with pytest.raises(ValueError):
            create_ui_factory("linux")

