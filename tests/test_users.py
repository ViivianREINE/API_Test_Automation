"""Test cases for User API endpoints."""

import json
import time
from utils.logger import log


def test_get_users(api_client):
    """Test GET /users endpoint - retrieve all users."""
    log("Testing GET /users API")
    
    response = api_client.get("/users")
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    log(f"✓ Successfully retrieved {len(response.json())} users")


def test_create_user(api_client):
    """Test POST /users endpoint - create a new user."""
    log("Testing POST /users API")
    
    payload = {
        "name": "Priyam",
        "email": "priyam@test.com"
    }
    
    response = api_client.post("/users", payload)
    
    assert response.status_code == 201
    assert response.json()["name"] == "Priyam"
    log(f"✓ User created successfully with ID: {response.json().get('id')}")


def test_create_multiple_users(api_client):
    """Test data-driven testing - create multiple users from JSON file."""
    log("Testing data-driven test with multiple users")
    
    with open("data/test_data.json", "r") as f:
        users = json.load(f)
    
    for user in users:
        response = api_client.post("/users", user)
        assert response.status_code == 201
        log(f"✓ Created user: {user['name']}")


def test_get_user_by_id(api_client):
    """Test GET /users/{id} endpoint - retrieve a specific user."""
    log("Testing GET /users/1 API")
    
    response = api_client.get("/users/1")
    
    assert response.status_code == 200
    assert response.json()["id"] == 1
    log(f"✓ Retrieved user: {response.json()['name']}")


def test_update_user(api_client):
    """Test PUT /users/{id} endpoint - update a user."""
    log("Testing PUT /users/1 API")
    
    payload = {
        "name": "UpdatedUser",
        "email": "updated@test.com"
    }
    
    response = api_client.put("/users/1", payload)
    
    assert response.status_code == 200
    assert response.json()["name"] == "UpdatedUser"
    log(f"✓ User updated successfully")


def test_delete_user(api_client):
    """Test DELETE /users/{id} endpoint - delete a user."""
    log("Testing DELETE /users/1 API")
    
    response = api_client.delete("/users/1")
    
    assert response.status_code == 200
    log(f"✓ User deleted successfully")


def test_response_time_performance(api_client):
    """Test response time performance - ensure requests complete within threshold."""
    log("Testing API response time performance")
    
    response = api_client.get("/users")
    response_time = response.elapsed.total_seconds()
    
    assert response.status_code == 200
    assert response_time < 2
    log(f"✓ Response completed in {response_time:.2f} seconds")
