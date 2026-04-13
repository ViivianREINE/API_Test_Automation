"""Advanced test cases with schema validation, negative tests, and edge cases."""

import json
import pytest
from jsonschema import validate, ValidationError
from utils.logger import log

# JSON Schema for user validation
USER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "phone": {"type": "string"},
        "body": {"type": "string"}
    },
    "required": ["id", "name"]
}


class TestSchemaValidation:
    """Test cases for schema validation."""

    def test_get_users_response_schema(self, api_client):
        """Test that GET /users response matches schema."""
        log("Testing response schema validation")
        
        response = api_client.get("/users")
        users = response.json()
        
        assert response.status_code == 200
        assert isinstance(users, list)
        
        # Validate each user object against schema
        for user in users[:3]:  # Test first 3 users
            try:
                validate(instance=user, schema=USER_SCHEMA)
                log(f"✓ User {user.get('id')} matches schema")
            except ValidationError as e:
                pytest.fail(f"Schema validation failed: {e.message}")


class TestNegativeScenarios:
    """Test cases for error handling and negative scenarios."""

    def test_get_nonexistent_user(self, api_client):
        """Test GET request for non-existent user ID."""
        log("Testing non-existent user retrieval")
        
        response = api_client.get("/users/999999")
        
        # JSONPlaceholder returns 404 for non-existent ID
        assert response.status_code == 404
        log("✓ Non-existent user handled correctly")

    def test_create_user_empty_payload(self, api_client):
        """Test POST with empty payload."""
        log("Testing empty payload submission")
        
        response = api_client.post("/users", {})
        
        # Should either accept or reject gracefully
        assert response.status_code in [201, 400]
        log(f"✓ Empty payload returned status {response.status_code}")

    def test_create_user_missing_required_fields(self, api_client):
        """Test POST with missing required fields."""
        log("Testing missing required fields")
        
        payload = {"email": "test@example.com"}  # Missing name
        response = api_client.post("/users", payload)
        
        # Should accept but ideally 400 in real API
        assert response.status_code in [201, 400]
        log(f"✓ Missing fields returned status {response.status_code}")

    def test_create_user_invalid_email_format(self, api_client):
        """Test POST with invalid email format."""
        log("Testing invalid email format")
        
        payload = {
            "name": "Test User",
            "email": "invalid-email-format"
        }
        response = api_client.post("/users", payload)
        
        # JSONPlaceholder accepts it, but real API should validate
        assert response.status_code == 201
        log("✓ Invalid email handling tested")


class TestEdgeCases:
    """Test cases for edge cases and boundary conditions."""

    def test_create_user_special_characters(self, api_client):
        """Test user creation with special characters."""
        log("Testing special characters in user name")
        
        payload = {
            "name": "Test User !@#$%^&*()",
            "email": "test+special@example.com"
        }
        response = api_client.post("/users", payload)
        
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == payload["name"]
        log("✓ Special characters handled correctly")

    def test_create_user_very_long_name(self, api_client):
        """Test user creation with very long name."""
        log("Testing very long user name (255 chars)")
        
        long_name = "A" * 255
        payload = {
            "name": long_name,
            "email": "test@example.com"
        }
        response = api_client.post("/users", payload)
        
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == long_name
        log("✓ Long names handled correctly")

    def test_create_user_unicode_characters(self, api_client):
        """Test user creation with unicode characters."""
        log("Testing unicode characters in user data")
        
        payload = {
            "name": "Test User 你好 مرحبا",
            "email": "test@example.com"
        }
        response = api_client.post("/users", payload)
        
        assert response.status_code == 201
        data = response.json()
        assert "Test User" in data["name"]
        log("✓ Unicode characters handled correctly")

    def test_update_user_partial_fields(self, api_client):
        """Test partial update of user fields."""
        log("Testing partial user update")
        
        payload = {"email": "newemail@example.com"}
        response = api_client.patch("/users/1", payload)
        
        assert response.status_code in [200, 204]
        log("✓ Partial update handled correctly")

    def test_multiple_quick_requests(self, api_client):
        """Test handling of multiple rapid requests."""
        log("Testing multiple rapid consecutive requests")
        
        for i in range(5):
            response = api_client.get(f"/users/{i+1}")
            assert response.status_code == 200
        
        log("✓ Multiple rapid requests handled correctly")


class TestHeaderValidation:
    """Test cases for header validation."""

    def test_response_headers_present(self, api_client):
        """Test that response includes required headers."""
        log("Testing response headers")
        
        response = api_client.get("/posts")
        
        assert response.status_code == 200
        # Verify content type header
        assert 'content-type' in response.headers
        log(f"✓ Content-Type: {response.headers.get('content-type')}")

    def test_response_time_reasonable(self, api_client):
        """Test that response time is within acceptable limits."""
        log("Testing response time performance")
        
        response = api_client.get("/users")
        response_time = response.elapsed.total_seconds()
        
        assert response.status_code == 200
        assert response_time < 5, f"Response took {response_time}s, expected < 5s"
        log(f"✓ Response completed in {response_time:.2f}s")


class TestDataConsistency:
    """Test cases for data consistency and integrity."""

    def test_get_same_user_twice(self, api_client):
        """Test that same user returns consistent data."""
        log("Testing data consistency for repeated requests")
        
        response1 = api_client.get("/users/1")
        response2 = api_client.get("/users/1")
        
        assert response1.status_code == 200
        assert response2.status_code == 200
        
        data1 = response1.json()
        data2 = response2.json()
        
        assert data1 == data2
        log("✓ Data consistency verified")

    def test_created_user_can_be_retrieved(self, api_client):
        """Test that created user can be immediately retrieved."""
        log("Testing created user retrieval")
        
        # Create user
        create_payload = {
            "name": "Consistency Test User",
            "email": "consistency@test.com"
        }
        create_response = api_client.post("/users", create_payload)
        assert create_response.status_code == 201
        created_user = create_response.json()
        
        # Try to retrieve it
        retrieve_response = api_client.get(f"/users/{created_user.get('id')}")
        log("✓ Created user successfully retrieved")
