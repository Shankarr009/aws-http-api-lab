# API Documentation

Complete API reference for the User Management API.

## Base URL

```
https://{api-id}.execute-api.{region}.amazonaws.com
```

Replace `{api-id}` and `{region}` with your actual API Gateway values.

## Authentication

Currently, this API does not require authentication. For production use, consider implementing:
- Amazon Cognito
- API Keys
- IAM authorization

---

## Endpoints

### 1. Create User

Creates a new user in the system.

**Endpoint**: `POST /user`

**Request Headers**:
```
Content-Type: application/json
```

**Request Body**:
```json
{
  "userId": "string (required)",
  "name": "string (required)",
  "email": "string (required)"
}
```

**Example Request**:
```bash
curl -X POST https://your-api-id.execute-api.region.amazonaws.com/user \
  -H "Content-Type: application/json" \
  -d '{
    "userId": "101",
    "name": "Shankar Suthar",
    "email": "shankarsuthar499@gmail.com"
  }'
```

**Success Response** (201 Created):
```json
{
  "message": "User created successfully"
}
```

**Error Responses**:

400 Bad Request - Missing required fields:
```json
{
  "error": "Missing required field: userId"
}
```

500 Internal Server Error:
```json
{
  "error": "Internal server error message"
}
```

---

### 2. Get User

Retrieves a user by their userId.

**Endpoint**: `GET /user/{userId}`

**Path Parameters**:
- `userId` (string, required): The unique identifier of the user

**Example Request**:
```bash
curl -X GET https://your-api-id.execute-api.region.amazonaws.com/user/101
```

**Success Response** (200 OK):
```json
{
  "userId": "101",
  "name": "Shankar Suthar",
  "email": "shankarsuthar499@gmail.com"
}
```

**Error Responses**:

404 Not Found - User doesn't exist:
```json
{
  "message": "User not found"
}
```

400 Bad Request - Missing userId:
```json
{
  "error": "Missing required parameter: userId"
}
```

500 Internal Server Error:
```json
{
  "error": "Internal server error message"
}
```

---

### 3. Delete User

Deletes a user from the system.

**Endpoint**: `DELETE /user/{userId}`

**Path Parameters**:
- `userId` (string, required): The unique identifier of the user to delete

**Example Request**:
```bash
curl -X DELETE https://your-api-id.execute-api.region.amazonaws.com/user/101
```

**Success Response** (200 OK):
```json
{
  "message": "User 101 deleted successfully"
}
```

**Error Responses**:

400 Bad Request - Missing userId:
```json
{
  "error": "Missing required parameter: userId"
}
```

500 Internal Server Error:
```json
{
  "error": "Internal server error message"
}
```

**Note**: The delete operation returns success even if the user doesn't exist (idempotent operation).

---

## Data Model

### User Object

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| userId | String | Yes | Unique identifier for the user |
| name | String | Yes | User's full name |
| email | String | Yes | User's email address |

**Example**:
```json
{
  "userId": "101",
  "name": "Shankar Suthar",
  "email": "shankarsuthar499@gmail.com"
}
```

---

## HTTP Status Codes

| Code | Description |
|------|-------------|
| 200 | OK - Request successful |
| 201 | Created - Resource created successfully |
| 400 | Bad Request - Invalid input |
| 404 | Not Found - Resource not found |
| 500 | Internal Server Error - Server error |

---

## CORS Headers

All endpoints return the following CORS headers:

```
Access-Control-Allow-Origin: *
Content-Type: application/json
```

For production, restrict `Access-Control-Allow-Origin` to specific domains.

---

## Rate Limiting

API Gateway HTTP APIs have the following default limits:

- **Burst**: 5,000 requests
- **Steady-state**: 10,000 requests per second

For production, consider implementing:
- Usage plans
- API keys
- Throttling settings

---

## Error Handling

All errors follow this structure:

```json
{
  "error": "Error description"
}
```

Or:

```json
{
  "message": "Error description"
}
```

---

## Postman Collection

### Create User
```json
{
  "name": "Create User",
  "request": {
    "method": "POST",
    "header": [
      {
        "key": "Content-Type",
        "value": "application/json"
      }
    ],
    "body": {
      "mode": "raw",
      "raw": "{\n  \"userId\": \"101\",\n  \"name\": \"Shankar Suthar\",\n  \"email\": \"shankarsuthar499@gmail.com\"\n}"
    },
    "url": {
      "raw": "{{base_url}}/user",
      "host": ["{{base_url}}"],
      "path": ["user"]
    }
  }
}
```

### Get User
```json
{
  "name": "Get User",
  "request": {
    "method": "GET",
    "url": {
      "raw": "{{base_url}}/user/101",
      "host": ["{{base_url}}"],
      "path": ["user", "101"]
    }
  }
}
```

### Delete User
```json
{
  "name": "Delete User",
  "request": {
    "method": "DELETE",
    "url": {
      "raw": "{{base_url}}/user/101",
      "host": ["{{base_url}}"],
      "path": ["user", "101"]
    }
  }
}
```

**Postman Environment Variable**:
```json
{
  "base_url": "https://your-api-id.execute-api.region.amazonaws.com"
}
```

---

## Testing Examples

### Using cURL

**Create User**:
```bash
curl -X POST https://your-api-id.execute-api.region.amazonaws.com/user \
  -H "Content-Type: application/json" \
  -d '{"userId":"101","name":"Shankar Suthar","email":"shankarsuthar499@gmail.com"}'
```

**Get User**:
```bash
curl -X GET https://your-api-id.execute-api.region.amazonaws.com/user/101
```

**Delete User**:
```bash
curl -X DELETE https://your-api-id.execute-api.region.amazonaws.com/user/101
```

### Using Python Requests

```python
import requests
import json

base_url = "https://your-api-id.execute-api.region.amazonaws.com"

# Create User
create_response = requests.post(
    f"{base_url}/user",
    json={
        "userId": "101",
        "name": "Shankar Suthar",
        "email": "shankarsuthar499@gmail.com"
    }
)
print(create_response.json())

# Get User
get_response = requests.get(f"{base_url}/user/101")
print(get_response.json())

# Delete User
delete_response = requests.delete(f"{base_url}/user/101")
print(delete_response.json())
```

### Using JavaScript Fetch

```javascript
const baseUrl = "https://your-api-id.execute-api.region.amazonaws.com";

// Create User
fetch(`${baseUrl}/user`, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    userId: "101",
    name: "Shankar Suthar",
    email: "shankarsuthar499@gmail.com"
  })
})
.then(response => response.json())
.then(data => console.log(data));

// Get User
fetch(`${baseUrl}/user/101`)
  .then(response => response.json())
  .then(data => console.log(data));

// Delete User
fetch(`${baseUrl}/user/101`, {
  method: 'DELETE'
})
.then(response => response.json())
.then(data => console.log(data));
```

---

## Best Practices

1. **Input Validation**:
   - Validate userId format (e.g., alphanumeric only)
   - Validate email format
   - Check for required fields

2. **Error Handling**:
   - Always return appropriate HTTP status codes
   - Include descriptive error messages
   - Log errors to CloudWatch

3. **Security**:
   - Implement authentication (Cognito)
   - Use API keys for tracking
   - Enable AWS WAF for protection
   - Restrict CORS origins

4. **Performance**:
   - Use DynamoDB on-demand billing for variable workloads
   - Implement caching with API Gateway
   - Monitor with CloudWatch metrics

5. **Monitoring**:
   - Enable CloudWatch Logs
   - Set up alarms for errors
   - Track API usage metrics
   - Monitor DynamoDB metrics

---

## Limitations

Current implementation limitations:

1. ❌ No authentication/authorization
2. ❌ No input validation beyond required fields
3. ❌ No pagination for listing users
4. ❌ No update (PUT/PATCH) operation
5. ❌ No email format validation
6. ❌ No duplicate user checking

**Future Enhancements**:
- Add Amazon Cognito authentication
- Implement request validation
- Add UPDATE user endpoint
- Add LIST users with pagination
- Implement proper error codes
- Add request/response logging

---

## Versioning

Current Version: **v1.0.0**

Future versions will maintain backward compatibility or be released under a new API path (e.g., `/v2/user`).

---

## Support

For issues or questions:
- Check [Setup Guide](setup-guide.md)
- Review [Troubleshooting](#troubleshooting) section
- Contact: shankarsuthar499@gmail.com

---

## License

This API is part of the AWS HTTP API Lab project - MIT License
