"""Pytest configuration and fixtures for API Test Automation Framework."""

import pytest
from utils.api_client import APIClient
from utils.config import get_config


@pytest.fixture
def api_client():
    """
    Fixture to provide APIClient instance for all tests.
    
    Automatically uses configuration from environment variables:
    - BASE_URL: Override API base URL
    - ENV: Set environment (dev, staging, prod)
    """
    config = get_config()
    return APIClient(base_url=config.BASE_URL)


@pytest.fixture
def sample_user_payload():
    """Fixture providing sample user data for tests."""
    return {
        "name": "Test User",
        "email": "test@example.com",
        "phone": "1234567890"
    }


@pytest.fixture
def authenticated_api_client():
    """Fixture providing authenticated API client with JWT token."""
    api_client = APIClient()
    # Note: In real scenario, get token from login endpoint or env variable
    api_client.set_token("sample-jwt-token")
    return api_client
