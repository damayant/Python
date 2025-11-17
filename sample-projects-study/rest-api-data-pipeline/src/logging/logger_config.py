"""Logger configuration module for REST API Data Pipeline."""

import logging
import logging.handlers
from pathlib import Path
from typing import Optional


class LoggerConfig:
    """Configuration class for logger setup with both console and file handlers."""

    DEFAULT_LOG_FORMAT = (
        "[%(asctime)s] - %(name)s - %(levelname)s - %(message)s"
    )
    DEFAULT_LOG_LEVEL = logging.INFO

    def __init__(
        self,
        name: str,
        log_level: int = DEFAULT_LOG_LEVEL,
        log_dir: Optional[Path] = None,
        enable_file_logging: bool = True,
    ):
        """Initialize logger configuration.

        Args:
            name: Logger name
            log_level: Logging level (default: INFO)
            log_dir: Directory for log files (default: ./logs)
            enable_file_logging: Whether to enable file logging
        """
        self.name = name
        self.log_level = log_level
        self.log_dir = log_dir or Path("logs")
        self.enable_file_logging = enable_file_logging
        self._validate_log_level()

    def _validate_log_level(self) -> None:
        """Validate that log level is a valid integer."""
        if not isinstance(self.log_level, int):
            raise ValueError(
                f"log_level must be int, got {type(self.log_level).__name__}"
            )

    def create_logger(self) -> logging.Logger:
        """Create and configure logger with console and optional file handlers.

        Returns:
            Configured logger instance
        """
        logger = logging.getLogger(self.name)
        logger.setLevel(self.log_level)

        # Clear existing handlers
        logger.handlers.clear()

        # Create formatters
        formatter = logging.Formatter(self.DEFAULT_LOG_FORMAT)

        # Add console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(self.log_level)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # Add file handler if enabled
        if self.enable_file_logging:
            self._setup_file_handler(logger, formatter)

        return logger

    def _setup_file_handler(
        self, logger: logging.Logger, formatter: logging.Formatter
    ) -> None:
        """Setup file handler with rotation.

        Args:
            logger: Logger instance to add handler to
            formatter: Log formatter
        """
        # Create log directory if it doesn't exist
        self.log_dir.mkdir(parents=True, exist_ok=True)

        # Create rotating file handler
        log_file = self.log_dir / f"{self.name}.log"
        file_handler = logging.handlers.RotatingFileHandler(
            log_file,
            maxBytes=10 * 1024 * 1024,  # 10MB
            backupCount=5,
        )
        file_handler.setLevel(self.log_level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)


def setup_logger(
    name: str,
    log_level: Optional[int] = None,
    enable_file_logging: bool = True,
) -> logging.Logger:
    """Setup logger with default or custom configuration.

    Args:
        name: Logger name (typically __name__)
        log_level: Logging level (default: INFO)
        enable_file_logging: Whether to enable file logging

    Returns:
        Configured logger instance

    Example:
        >>> logger = setup_logger(__name__)
        >>> logger.info("Application started")
    """
    log_level = log_level or LoggerConfig.DEFAULT_LOG_LEVEL
    config = LoggerConfig(
        name=name,
        log_level=log_level,
        enable_file_logging=enable_file_logging,
    )
    return config.create_logger()

