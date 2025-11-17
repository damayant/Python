"""Custom exceptions for API client module."""


class APIError(Exception):
    """Base exception for API-related errors."""

    def __init__(self, message: str, status_code: int = None):
        """Initialize APIError.

        Args:
            message: Error message
            status_code: HTTP status code (optional)
        """
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class ValidationError(APIError):
    """Exception raised when data validation fails."""

    pass


class NetworkError(APIError):
    """Exception raised for network-related errors."""

    pass


class TimeoutError(APIError):
    """Exception raised when API request times out."""

    pass

