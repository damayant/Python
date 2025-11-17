"""Tests for logging module."""

import logging
import tempfile
from pathlib import Path

import pytest

from src.logging import setup_logger
from src.logging.logger_config import LoggerConfig


class TestLoggerConfig:
    """Test cases for LoggerConfig."""

    def test_initialization(self):
        """Test LoggerConfig initialization."""
        config = LoggerConfig("test_logger")
        assert config.name == "test_logger"
        assert config.log_level == logging.INFO

    def test_initialization_with_custom_level(self):
        """Test initialization with custom log level."""
        config = LoggerConfig("test_logger", log_level=logging.DEBUG)
        assert config.log_level == logging.DEBUG

    def test_initialization_invalid_log_level(self):
        """Test initialization with invalid log level."""
        with pytest.raises(ValueError):
            LoggerConfig("test_logger", log_level="INVALID")

    def test_create_logger(self):
        """Test creating logger."""
        config = LoggerConfig("test_logger", enable_file_logging=False)
        logger = config.create_logger()
        assert logger.name == "test_logger"
        assert logger.level == logging.INFO

    def test_create_logger_with_file_handler(self):
        """Test creating logger with file handler."""
        with tempfile.TemporaryDirectory() as temp_dir:
            log_dir = Path(temp_dir)
            config = LoggerConfig(
                "test_logger",
                log_dir=log_dir,
                enable_file_logging=True,
            )
            logger = config.create_logger()

            # Check that file handler was added
            file_handlers = [h for h in logger.handlers
                           if isinstance(h, logging.handlers.RotatingFileHandler)]
            assert len(file_handlers) > 0

            # Write a log message
            logger.info("Test message")

            # Check that log file was created
            log_file = log_dir / "test_logger.log"
            assert log_file.exists()

    def test_logger_handlers(self):
        """Test that logger has expected handlers."""
        config = LoggerConfig("test_logger", enable_file_logging=False)
        logger = config.create_logger()

        # Should have at least one handler (console)
        assert len(logger.handlers) >= 1

        # Check for stream handler
        stream_handlers = [h for h in logger.handlers
                          if isinstance(h, logging.StreamHandler)]
        assert len(stream_handlers) > 0


class TestSetupLogger:
    """Test cases for setup_logger function."""

    def test_setup_logger_default(self):
        """Test setup_logger with default configuration."""
        logger = setup_logger("test_app", enable_file_logging=False)
        assert logger.name == "test_app"
        assert logger.level == logging.INFO

    def test_setup_logger_debug_level(self):
        """Test setup_logger with debug level."""
        logger = setup_logger(
            "test_app",
            log_level=logging.DEBUG,
            enable_file_logging=False,
        )
        assert logger.level == logging.DEBUG

    def test_setup_logger_messages(self):
        """Test logging messages at different levels."""
        logger = setup_logger("test_app", enable_file_logging=False)

        # These should not raise any exceptions
        logger.debug("Debug message")
        logger.info("Info message")
        logger.warning("Warning message")
        logger.error("Error message")

    def test_multiple_loggers(self):
        """Test creating multiple loggers."""
        logger1 = setup_logger("app1", enable_file_logging=False)
        logger2 = setup_logger("app2", enable_file_logging=False)

        assert logger1.name == "app1"
        assert logger2.name == "app2"
        assert logger1 != logger2

