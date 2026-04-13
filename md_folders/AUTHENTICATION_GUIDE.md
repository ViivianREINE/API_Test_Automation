"""Authentication examples for API Test Automation Framework."""

import pytest
from utils.api_client import APIClient


class TestAuthenticationPatterns:
    """Examples of different authentication patterns."""

    def test_bearer_token_auth(self):
        """Example: Bearer Token Authentication."""
        api_client = APIClient()
        
        # Set Bearer token
        jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
        api_client.set_token(jwt_token, token_type="Bearer")
        
        # Make authenticated request
        response = api_client.get("/protected-resource")
        assert response.status_code == 200

    def test_api_key_auth(self):
        """Example: API Key Authentication."""
        api_client = APIClient()
        
        # Set API key as custom header
        api_client.set_header("X-API-Key", "your-api-key-here")
        
        response = api_client.get("/data")
        assert response.status_code == 200

    def test_oauth_token_auth(self):
        """Example: OAuth Token Authentication."""
        api_client = APIClient()
        
        # OAuth typically uses Bearer with specific token format
        oauth_token = "access_token_from_oauth_provider"
        api_client.set_token(oauth_token, token_type="Bearer")
        
        response = api_client.get("/oauth-protected")
        assert response.status_code == 200

    def test_custom_auth_header(self):
        """Example: Custom Authentication Header."""
        api_client = APIClient()
        
        # Set custom auth header
        api_client.set_header("Authorization", "Custom-Auth xyz123")
        
        response = api_client.get("/custom-auth-endpoint")
        assert response.status_code == 200

    def test_multiple_headers(self):
        """Example: Multiple Headers (Auth + Custom)."""
        api_client = APIClient()
        
        # Set JWT token
        api_client.set_token("jwt-token-here")
        
        # Add additional headers
        api_client.set_header("X-Request-ID", "unique-request-id-123")
        api_client.set_header("X-Client-Version", "1.0.0")
        
        response = api_client.get("/endpoint")
        assert response.status_code == 200

    def test_basic_auth(self):
        """Example: Basic Authentication."""
        import base64
        api_client = APIClient()
        
        # Basic auth: base64(username:password)
        username = "user"
        password = "pass"
        credentials = base64.b64encode(f"{username}:{password}".encode()).decode()
        
        api_client.set_header("Authorization", f"Basic {credentials}")
        
        response = api_client.get("/secure")
        assert response.status_code == 200

    def test_login_and_use_token(self):
        """Example: Login to get token, then use it."""
        api_client = APIClient()
        
        # Step 1: Login to get token
        login_payload = {
            "username": "testuser@example.com",
            "password": "password123"
        }
        login_response = api_client.post("/auth/login", login_payload)
        assert login_response.status_code == 200
        
        # Extract token from response
        token = login_response.json().get("token")
        
        # Step 2: Set token for authenticated requests
        api_client.set_token(token)
        
        # Step 3: Make authenticated requests
        response = api_client.get("/user/profile")
        assert response.status_code == 200

    def test_refresh_token_flow(self):
        """Example: Refresh token when expired."""
        api_client = APIClient()
        
        # Initial request with access token
        access_token = "initial-access-token"
        api_client.set_token(access_token)
        
        response = api_client.get("/data")
        
        # If 401, refresh the token
        if response.status_code == 401:
            refresh_response = api_client.post(
                "/auth/refresh",
                {"refresh_token": "your-refresh-token"}
            )
            
            if refresh_response.status_code == 200:
                new_token = refresh_response.json().get("access_token")
                api_client.set_token(new_token)
                
                # Retry with new token
                response = api_client.get("/data")
        
        assert response.status_code == 200

    def test_token_in_query_param(self):
        """Example: Token in Query Parameter (not recommended)."""
        api_client = APIClient()
        
        # Some APIs accept token as query parameter (not best practice)
        response = api_client.get("/data?token=your-token-here")
        assert response.status_code == 200

    def test_session_based_auth(self):
        """Example: Session-based Authentication."""
        api_client = APIClient()
        
        # Login to establish session
        login_payload = {
            "username": "user@example.com",
            "password": "password"
        }
        login_response = api_client.post("/login", login_payload)
        assert login_response.status_code == 200
        
        # Session cookie is automatically handled by requests
        # Further requests will use the session
        response = api_client.get("/dashboard")
        assert response.status_code == 200


@pytest.fixture
def authenticated_client():
    """
    Fixture: Already authenticated API client.
    
    Usage in tests:
        def test_something(authenticated_client):
            response = authenticated_client.get("/protected")
    """
    api_client = APIClient()
    
    # Perform login
    login_response = api_client.post(
        "/auth/login",
        {"username": "test@example.com", "password": "password"}
    )
    
    if login_response.status_code == 200:
        token = login_response.json().get("token")
        api_client.set_token(token)
    
    return api_client


class TestWithFixtures:
    """Test examples using authenticated client fixture."""

    def test_protected_endpoint(self, authenticated_client):
        """Test protected endpoint with authenticated client."""
        response = authenticated_client.get("/protected-resource")
        assert response.status_code == 200


# Best Practices
"""
✅ DO:
   - Use environment variables for sensitive tokens
   - Use fixtures for token setup
   - Refresh tokens when expired
   - Log authentication attempts (without tokens)
   - Use HTTPS for all requests
   - Store tokens securely

❌ DON'T:
   - Hardcode tokens in test files
   - Log sensitive tokens
   - Use URL parameters for secrets
   - Share tokens across tests unnecessarily
   - Use HTTP for sensitive data
   - Keep old tokens in code
"""
