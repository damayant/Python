"""API client module with support for both stateless and stateful operations."""

import logging
from abc import ABC, abstractmethod
from typing import Any, Dict, Generator, Optional

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from .exceptions import APIError, NetworkError, TimeoutError, ValidationError


class BaseAPIClient(ABC):
    """Abstract base class for API clients."""

    DEFAULT_TIMEOUT = 30
    DEFAULT_RETRIES = 3

    def __init__(
        self,
        base_url: str,
        timeout: int = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_RETRIES,
    ):
        """Initialize API client.

        Args:
            base_url: Base URL for API
            timeout: Request timeout in seconds
            max_retries: Maximum number of retries
        """
        if not base_url:
            raise ValidationError("base_url cannot be empty")

        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    def get(self, endpoint: str, **kwargs) -> Dict[str, Any]:
        """GET request to API.

        Args:
            endpoint: API endpoint
            **kwargs: Additional arguments

        Returns:
            Response data as dictionary
        """
        pass


class StatelessAPIClient(BaseAPIClient):
    """Stateless API client - each request is independent.

    This client does not maintain state between requests.
    Each request is a complete, independent operation.
    """

    def __init__(
        self,
        base_url: str,
        timeout: int = BaseAPIClient.DEFAULT_TIMEOUT,
        max_retries: int = BaseAPIClient.DEFAULT_RETRIES,
    ):
        """Initialize stateless API client."""
        super().__init__(base_url, timeout, max_retries)
        self.logger.info(f"Initialized StatelessAPIClient with base_url: {base_url}")

    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        """Make GET request to endpoint.

        Args:
            endpoint: API endpoint
            params: Query parameters

        Returns:
            Response JSON as dictionary

        Raises:
            ValidationError: If endpoint is invalid
            NetworkError: If network error occurs
            TimeoutError: If request times out
        """
        if not endpoint:
            raise ValidationError("endpoint cannot be empty")

        url = self._build_url(endpoint)
        self.logger.debug(f"GET request to {url} with params: {params}")

        try:
            response = requests.get(
                url,
                params=params or {},
                timeout=self.timeout,
                headers=self._get_headers(),
            )
            response.raise_for_status()
            return response.json()

        except requests.exceptions.Timeout as e:
            error_msg = f"Request to {url} timed out after {self.timeout}s"
            self.logger.error(error_msg)
            raise TimeoutError(error_msg)

        except requests.exceptions.ConnectionError as e:
            error_msg = f"Connection error to {url}: {str(e)}"
            self.logger.error(error_msg)
            raise NetworkError(error_msg)

        except requests.exceptions.HTTPError as e:
            status_code = e.response.status_code
            error_msg = f"HTTP {status_code} from {url}"
            self.logger.error(error_msg)
            raise APIError(error_msg, status_code)

        except requests.exceptions.RequestException as e:
            error_msg = f"Request error to {url}: {str(e)}"
            self.logger.error(error_msg)
            raise APIError(error_msg)

    def get_paginated(
        self,
        endpoint: str,
        page_param: str = "page",
        limit_param: str = "limit",
        limit: int = 10,
    ) -> Generator[Dict[str, Any], None, None]:
        """Fetch paginated data from endpoint.

        Yields data page by page without maintaining state.
        Each page fetch is an independent request.

        Args:
            endpoint: API endpoint
            page_param: Parameter name for page number
            limit_param: Parameter name for page size
            limit: Number of items per page

        Yields:
            Data from each page
        """
        page = 1
        while True:
            params = {page_param: page, limit_param: limit}
            try:
                data = self.get(endpoint, params)
                if not data or (isinstance(data, dict) and not data.get("items")):
                    break
                yield data
                page += 1
            except APIError as e:
                self.logger.error(f"Error fetching page {page}: {e}")
                break

    def _build_url(self, endpoint: str) -> str:
        """Build full URL from base URL and endpoint.

        Args:
            endpoint: API endpoint

        Returns:
            Full URL
        """
        endpoint = endpoint.lstrip("/")
        return f"{self.base_url}/{endpoint}"

    def _get_headers(self) -> Dict[str, str]:
        """Get default headers for requests.

        Returns:
            Dictionary of headers
        """
        return {"Content-Type": "application/json"}


class StatefulAPIClient(BaseAPIClient):
    """Stateful API client - maintains state across requests.

    This client maintains context across multiple operations,
    such as authentication tokens, session data, etc.
    """

    def __init__(
        self,
        base_url: str,
        timeout: int = BaseAPIClient.DEFAULT_TIMEOUT,
        max_retries: int = BaseAPIClient.DEFAULT_RETRIES,
    ):
        """Initialize stateful API client."""
        super().__init__(base_url, timeout, max_retries)
        self._session = self._create_session()
        self._state: Dict[str, Any] = {}
        self.logger.info(f"Initialized StatefulAPIClient with base_url: {base_url}")

    def _create_session(self) -> requests.Session:
        """Create requests session with retry strategy.

        Returns:
            Configured requests.Session
        """
        session = requests.Session()

        # Configure retry strategy
        retry_strategy = Retry(
            total=self.max_retries,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)

        return session

    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        """Make GET request using session.

        Args:
            endpoint: API endpoint
            params: Query parameters

        Returns:
            Response JSON as dictionary

        Raises:
            ValidationError: If endpoint is invalid
            NetworkError: If network error occurs
            TimeoutError: If request times out
        """
        if not endpoint:
            raise ValidationError("endpoint cannot be empty")

        url = self._build_url(endpoint)
        self.logger.debug(f"GET request (stateful) to {url}")

        try:
            response = self._session.get(
                url,
                params=params or {},
                timeout=self.timeout,
                headers=self._get_headers(),
            )
            response.raise_for_status()
            data = response.json()
            self._update_state(data)
            return data

        except requests.exceptions.Timeout as e:
            error_msg = f"Request to {url} timed out after {self.timeout}s"
            self.logger.error(error_msg)
            raise TimeoutError(error_msg)

        except requests.exceptions.ConnectionError as e:
            error_msg = f"Connection error to {url}: {str(e)}"
            self.logger.error(error_msg)
            raise NetworkError(error_msg)

        except requests.exceptions.HTTPError as e:
            status_code = e.response.status_code
            error_msg = f"HTTP {status_code} from {url}"
            self.logger.error(error_msg)
            raise APIError(error_msg, status_code)

        except requests.exceptions.RequestException as e:
            error_msg = f"Request error to {url}: {str(e)}"
            self.logger.error(error_msg)
            raise APIError(error_msg)

    def set_state(self, key: str, value: Any) -> None:
        """Set state value.

        Args:
            key: State key
            value: State value
        """
        self._state[key] = value
        self.logger.debug(f"State updated: {key}")

    def get_state(self, key: str, default: Any = None) -> Any:
        """Get state value.

        Args:
            key: State key
            default: Default value if key not found

        Returns:
            State value or default
        """
        return self._state.get(key, default)

    def _update_state(self, data: Dict[str, Any]) -> None:
        """Update internal state based on response data.

        Args:
            data: Response data
        """
        if isinstance(data, dict):
            if "pagination" in data:
                self.set_state("last_pagination", data["pagination"])

    def _build_url(self, endpoint: str) -> str:
        """Build full URL from base URL and endpoint.

        Args:
            endpoint: API endpoint

        Returns:
            Full URL
        """
        endpoint = endpoint.lstrip("/")
        return f"{self.base_url}/{endpoint}"

    def _get_headers(self) -> Dict[str, str]:
        """Get headers including any state-based headers.

        Returns:
            Dictionary of headers
        """
        headers = {"Content-Type": "application/json"}
        return headers

    def close(self) -> None:
        """Close the session."""
        if self._session:
            self._session.close()
            self.logger.info("Session closed")

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()

