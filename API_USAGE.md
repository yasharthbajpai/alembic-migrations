# User Management API

This document provides instructions on how to use the User Management API for fetching and inserting user data.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the database:**
   ```bash
   docker-compose up -d
   ```

3. **Run migrations:**
   ```bash
   alembic upgrade head
   ```

4. **Start the API server:**
   ```bash
   python run_api.py
   ```

The API will be available at `http://localhost:8000`

## API Endpoints

### 1. Fetch All Users (GET)
**URL:** `GET /users`

**Parameters:**
- `skip` (optional): Number of records to skip for pagination (default: 0)
- `limit` (optional): Maximum number of records to return (default: 100)

**Example:**
```bash
curl -X GET "http://localhost:8000/users?skip=0&limit=10"
```

**Response:**
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "email": "jane@example.com"
  }
]
```

### 2. Fetch User by ID (GET)
**URL:** `GET /users/{user_id}`

**Example:**
```bash
curl -X GET "http://localhost:8000/users/1"
```

**Response:**
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}
```

### 3. Insert New User (POST)
**URL:** `POST /users`

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@example.com"
}
```

**Example:**
```bash
curl -X POST "http://localhost:8000/users" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com"
  }'
```

**Response:**
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}
```

## Interactive API Documentation

Once the server is running, you can access the interactive API documentation at:
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## Error Handling

The API includes proper error handling:

- **400 Bad Request:** When trying to create a user with an email that already exists
- **404 Not Found:** When trying to fetch a user that doesn't exist
- **500 Internal Server Error:** For database or server errors

## Testing the API

You can test the API using:
1. The interactive docs at http://localhost:8000/docs
2. curl commands (as shown above)
3. Postman or any other API testing tool
4. Python requests library

Example Python test:
```python
import requests

# Insert a user
response = requests.post("http://localhost:8000/users", json={
    "name": "Test User",
    "email": "test@example.com"
})
print(response.json())

# Fetch all users
response = requests.get("http://localhost:8000/users")
print(response.json())
```