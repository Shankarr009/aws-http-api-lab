222222222# AWS HTTP API Lab - DynamoDB Integration

A hands-on lab demonstrating how to build a serverless REST API using AWS API Gateway (HTTP API), Lambda, and DynamoDB. This project implements a complete user management system with Create, Read, and Delete operations.

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Author](#author)
- [License](#license)

## 🎯 Overview

This lab demonstrates how a frontend application can interact with a backend database (DynamoDB) through APIs created using API Gateway and Lambda functions. It provides a practical understanding of how API requests flow from client → API Gateway → Lambda → DynamoDB.

## 🏗 Architecture

```
Mobile/Web App → API Gateway (HTTP API) → Lambda Functions → DynamoDB
```

The architecture includes:
- **API Gateway (HTTP API)**: Entry point for all API requests
- **Lambda Functions**: Serverless compute for business logic
  - CreateUserFunction
  - GetUserFunction
  - DeleteUserFunction
- **DynamoDB**: NoSQL database for storing user data
- **IAM Role**: Permissions for Lambda to access DynamoDB

## ✅ Prerequisites

- AWS Account with appropriate permissions
- AWS CLI configured (optional)
- Postman or any API testing tool
- Basic understanding of:
  - AWS Lambda
  - API Gateway
  - DynamoDB
  - Python 3.12

## 🚀 Features

- ✅ Create new users with userId, name, and email
- 🔍 Retrieve user information by userId
- ❌ Delete users by userId
- 📊 Serverless architecture with automatic scaling
- 🔐 IAM-based security for Lambda-DynamoDB access
- ⚡ HTTP API for low latency and cost-effective operations

## 📝 Setup Instructions

### Step 1: Create DynamoDB Table

1. Navigate to AWS Console → DynamoDB
2. Click **Create table**
3. Configure:
   - **Table name**: `UsersTable`
   - **Partition key**: `userId` (String)
   - Keep default settings (on-demand capacity)
4. Click **Create Table**

### Step 2: Create IAM Role

1. Go to IAM → Roles → **Create Role**
2. Select:
   - **Trusted entity type**: AWS service
   - **Use case**: Lambda
3. Attach policy: `AmazonDynamoDBFullAccess`
4. Name: `LambdaDynamoDBExecutionRole`
5. Create role

### Step 3: Create Lambda Functions

Create three Lambda functions with the following configuration:

#### Common Settings for All Functions:
- **Runtime**: Python 3.12
- **Permissions**: Use existing role → `LambdaDynamoDBExecutionRole`

#### 3.1 CreateUserFunction

- **Function name**: `CreateUserFunction`
- **Code**: See [lambda-functions/CreateUserFunction.py](lambda-functions/CreateUserFunction.py)

#### 3.2 GetUserFunction

- **Function name**: `GetUserFunction`
- **Code**: See [lambda-functions/GetUserFunction.py](lambda-functions/GetUserFunction.py)

#### 3.3 DeleteUserFunction

- **Function name**: `DeleteUserFunction`
- **Code**: See [lambda-functions/DeleteUserFunction.py](lambda-functions/DeleteUserFunction.py)

### Step 4: Create HTTP API in API Gateway

1. Go to API Gateway → **Create API**
2. Select **HTTP API** → Build
3. Configure:
   - **API name**: `UserAPI`
   - Click **Next** through default settings
   - **Create**

### Step 5: Configure Routes

Create the following routes:

| Method | Route | Lambda Function |
|--------|-------|----------------|
| POST | /user | CreateUserFunction |
| GET | /user/{userId} | GetUserFunction |
| DELETE | /user/{userId} | DeleteUserFunction |

#### Route 1: POST /user
1. Click **Routes** → **Create**
2. Method: **POST**, Path: `/user`
3. Attach integration → Lambda → `CreateUserFunction`

#### Route 2: GET /user/{userId}
1. Click **Routes** → **Create**
2. Method: **GET**, Path: `/user/{userId}`
3. Attach integration → Lambda → `GetUserFunction`

#### Route 3: DELETE /user/{userId}
1. Click **Routes** → **Create**
2. Method: **DELETE**, Path: `/user/{userId}`
3. Attach integration → Lambda → `DeleteUserFunction`

### Step 6: Get API Endpoint

1. Go to **Stages** → **$default**
2. Copy the **Invoke URL**
3. Format: `https://your-api-id.execute-api.region.amazonaws.com`

## 🔌 API Endpoints

### 1. Create User

**Endpoint**: `POST /user`

**Request Body**:
```json
{
  "userId": "101",
  "name": "Shankar Suthar",
  "email": "shankarsuthar499@gmail.com"
}
```

**Response**:
```json
{
  "statusCode": 201,
  "body": "{\"message\": \"User created successfully\"}"
}
```

### 2. Get User

**Endpoint**: `GET /user/{userId}`

**Example**: `GET /user/101`

**Response**:
```json
{
  "statusCode": 200,
  "body": "{\"userId\":\"101\",\"name\":\"Shankar Suthar\",\"email\":\"shankarsuthar499@gmail.com\"}"
}
```

### 3. Delete User

**Endpoint**: `DELETE /user/{userId}`

**Example**: `DELETE /user/101`

**Response**:
```json
{
  "statusCode": 200,
  "body": "{\"message\": \"User 101 deleted successfully\"}"
}
```

## 🧪 Testing

### Using Postman

1. **Create User**:
   - Method: POST
   - URL: `https://your-api-id.execute-api.region.amazonaws.com/user`
   - Headers: `Content-Type: application/json`
   - Body: Raw JSON (see example above)

2. **Get User**:
   - Method: GET
   - URL: `https://your-api-id.execute-api.region.amazonaws.com/user/101`

3. **Delete User**:
   - Method: DELETE
   - URL: `https://your-api-id.execute-api.region.amazonaws.com/user/101`

### Lambda Test Events

Test events for each Lambda function are provided in the [documentation](documentation/lambda-test-events.json) folder.

## 📁 Project Structure

```
aws-http-api-lab/
├── README.md
├── LICENSE
├── .gitignore
├── lambda-functions/
│   ├── CreateUserFunction.py
│   ├── GetUserFunction.py
│   └── DeleteUserFunction.py
├── documentation/
│   ├── lambda-test-events.json
│   ├── setup-guide.md
│   └── api-documentation.md
└── assets/
    └── architecture-diagram.md
```

## 🛠 Technologies Used

- **AWS Lambda**: Serverless compute service
- **Amazon API Gateway**: HTTP API for REST endpoints
- **Amazon DynamoDB**: NoSQL database
- **Python 3.12**: Lambda runtime
- **IAM**: Identity and Access Management
- **Boto3**: AWS SDK for Python

## 📚 Learning Outcomes

After completing this lab, you will understand:

- ✅ How API Gateway routes requests to Lambda functions
- ✅ How Lambda functions interact with DynamoDB
- ✅ Serverless architecture patterns
- ✅ HTTP API vs REST API differences (covered in next lab)
- ✅ IAM role permissions for AWS services
- ✅ Best practices for separating API logic (Separation of Concerns)

## 🔒 Security Best Practices

- Use IAM roles with least privilege principle
- Enable API Gateway throttling for production
- Implement request validation
- Use AWS Secrets Manager for sensitive data
- Enable CloudWatch logging for debugging

## 💡 Next Steps

- Implement REST API version for comparison
- Add authentication using Amazon Cognito
- Implement request/response validation
- Add error handling and logging
- Deploy using AWS SAM or CloudFormation
- Add unit tests for Lambda functions

## 👤 Author

**Shankar Suthar**
- GitHub: https://github.com/Shankarr009/aws-http-api-lab
- Email: shankarsuthar499@gmail.com

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- AWS Documentation
- CloudFolks for the lab structure and guidance
- AWS Community for best practices

## 📞 Support

If you have any questions or run into issues:
1. Check the [documentation](documentation/) folder
2. Review AWS CloudWatch logs for Lambda errors
3. Open an issue in this repository
4. Contact: shankarsuthar499@gmail.com

---

⭐ If you found this helpful, please star this repository!
