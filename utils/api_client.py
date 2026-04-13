"""API Client for making HTTP requests."""

import requests
from typing import Dict, Any, Optional
from utils.config import get_config


class APIClient:
    """API Client for making HTTP requests to the server."""

    def __init__(self, base_url: Optional[str] = None, timeout: int = 10):
        """
        Initialize API Client.
        
        Args:
            base_url: Base URL for API (uses config if not provided)
            timeout: Request timeout in seconds
        """
        config = get_config()
        self.base_url = base_url or config.BASE_URL
        self.timeout = timeout
        self.headers = {'Content-Type': 'application/json'}
        self.token = None

    def set_token(self, token: str, token_type: str = 'Bearer'):
        """
        Set authentication token.
        
        Args:
            token: Auth token
            token_type: Token type (default: Bearer)
        """
        self.token = token
        self.headers['Authorization'] = f'{token_type} {token}'

    def set_header(self, key: str, value: str):
        """Set custom header."""
        self.headers[key] = value

    def get(self, endpoint: str, params: Optional[Dict] = None):
        """Make a GET request."""
        url = f"{self.base_url}{endpoint}"
        return requests.get(
            url, 
            headers=self.headers, 
            params=params,
            timeout=self.timeout
        )

    def post(self, endpoint: str, payload: Optional[Dict] = None):
        """Make a POST request."""
        url = f"{self.base_url}{endpoint}"
        return requests.post(
            url, 
            json=payload,
            headers=self.headers,
            timeout=self.timeout
        )

    def put(self, endpoint: str, payload: Optional[Dict] = None):
        """Make a PUT request."""
        url = f"{self.base_url}{endpoint}"
        return requests.put(
            url, 
            json=payload,
            headers=self.headers,
            timeout=self.timeout
        )

    def patch(self, endpoint: str, payload: Optional[Dict] = None):
        """Make a PATCH request."""
        url = f"{self.base_url}{endpoint}"
        return requests.patch(
            url, 
            json=payload,
            headers=self.headers,
            timeout=self.timeout
        )

    def delete(self, endpoint: str):
        """Make a DELETE request."""
        url = f"{self.base_url}{endpoint}"
        return requests.delete(
            url,
            headers=self.headers,
            timeout=self.timeout
        )
