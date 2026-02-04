# Complete Setup Guide

This guide walks you through every step needed to deploy the AWS HTTP API Lab.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Part 1: Database Setup](#part-1-database-setup)
3. [Part 2: IAM Configuration](#part-2-iam-configuration)
4. [Part 3: Lambda Functions](#part-3-lambda-functions)
5. [Part 4: API Gateway](#part-4-api-gateway)
6. [Part 5: Testing](#part-5-testing)
7. [Troubleshooting](#troubleshooting)

---

## Prerequisites

Before starting, ensure you have:

- ✅ AWS Account with administrator access
- ✅ Basic knowledge of AWS Console
- ✅ Postman installed (or alternative API testing tool)
- ✅ Text editor for viewing/editing code

**Estimated Time**: 45-60 minutes

---

## Part 1: Database Setup

### Step 1.1: Create DynamoDB Table

1. **Navigate to DynamoDB**:
   - Open AWS Console
   - Search for "DynamoDB" in the services search bar
   - Click on DynamoDB

2. **Create Table**:
   - Click **Create table** button
   
3. **Configure Table Settings**:
   ```
   Table name: UsersTable
   Partition key: userId (String)
   Sort key: Leave blank
   ```

4. **Table Settings**:
   - **Table class**: Standard
   - **Capacity mode**: On-demand (for this lab)
   - Leave all other settings as default

5. **Create**:
   - Scroll down and click **Create table**
   - Wait for table status to become "Active" (usually 10-20 seconds)

### Step 1.2: Verify Table Creation

1. Click on the table name "UsersTable"
2. Go to **Explore table items** tab
3. You should see an empty table (no items yet)

---

## Part 2: IAM Configuration

### Step 2.1: Create IAM Role for Lambda

1. **Navigate to IAM**:
   - Open AWS Console
   - Search for "IAM"
   - Click on **Roles** in the left sidebar

2. **Create Role**:
   - Click **Create role** button

3. **Select Trusted Entity**:
   - **Trusted entity type**: AWS service
   - **Use case**: Lambda
   - Click **Next**

4. **Add Permissions**:
   - In the search box, type: `AmazonDynamoDBFullAccess`
   - Check the box next to **AmazonDynamoDBFullAccess**
   - Click **Next**

5. **Name and Create**:
   ```
   Role name: LambdaDynamoDBExecutionRole
   Description: Allows Lambda functions to access DynamoDB
   ```
   - Click **Create role**

### Step 2.2: Verify Role

1. Search for your role: `LambdaDynamoDBExecutionRole`
2. Click on it to view details
3. Verify that it has:
   - Trust relationship with Lambda service
   - AmazonDynamoDBFullAccess policy attached

---

## Part 3: Lambda Functions

You need to create **3 separate Lambda functions**. Follow these steps for each:

### Step 3.1: Create CreateUserFunction

1. **Navigate to Lambda**:
   - Open AWS Console
   - Search for "Lambda"
   - Click **Create function**

2. **Basic Information**:
   ```
   Option: Author from scratch
   Function name: CreateUserFunction
   Runtime: Python 3.12
   ```

3. **Permissions**:
   - Expand "Change default execution role"
   - Select **Use an existing role**
   - Choose: `LambdaDynamoDBExecutionRole`

4. **Create Function**:
   - Click **Create function**

5. **Add Code**:
   - In the Code source section, delete the default code
   - Copy the code from `lambda-functions/CreateUserFunction.py`
   - Paste it into the editor
   - Click **Deploy**

6. **Test the Function**:
   - Click **Test** button
   - Click **Create new test event**
   - Event name: `CreateUserTest`
   - Replace the JSON with:
   ```json
   {
     "body": "{\"userId\": \"101\", \"name\": \"Shankar Suthar\", \"email\": \"shankarsuthar499@gmail.com\"}"
   }
   ```
   - Click **Save**
   - Click **Test** again

7. **Verify Result**:
   - You should see a successful response:
   ```json
   {
     "statusCode": 201,
     "body": "{\"message\": \"User created successfully\"}"
   }
   ```
   - Go to DynamoDB → UsersTable → Explore items
   - You should see the new user record

### Step 3.2: Create GetUserFunction

1. **Create Function**:
   ```
   Function name: GetUserFunction
   Runtime: Python 3.12
   Existing role: LambdaDynamoDBExecutionRole
   ```

2. **Add Code**:
   - Copy code from `lambda-functions/GetUserFunction.py`
   - Paste and **Deploy**

3. **Test**:
   - Event name: `GetUserTest`
   - JSON:
   ```json
   {
     "pathParameters": {
       "userId": "101"
     }
   }
   ```
   - Should return the user data you created earlier

### Step 3.3: Create DeleteUserFunction

1. **Create Function**:
   ```
   Function name: DeleteUserFunction
   Runtime: Python 3.12
   Existing role: LambdaDynamoDBExecutionRole
   ```

2. **Add Code**:
   - Copy code from `lambda-functions/DeleteUserFunction.py`
   - Paste and **Deploy**

3. **Test**:
   - Event name: `DeleteUserTest`
   - JSON:
   ```json
   {
     "pathParameters": {
       "userId": "101"
     }
   }
   ```
   - Should return success message
   - Verify in DynamoDB that the item is deleted

---

## Part 4: API Gateway

### Step 4.1: Create HTTP API

1. **Navigate to API Gateway**:
   - Open AWS Console
   - Search for "API Gateway"
   - Click **Create API**

2. **Choose API Type**:
   - Find **HTTP API**
   - Click **Build**

3. **Configure API**:
   ```
   API name: UserAPI
   Description: User management API
   ```
   - Click **Next**

4. **Configure Routes** (Skip for now):
   - Click **Next**

5. **Configure Stages**:
   - Leave as `$default`
   - Click **Next**

6. **Review and Create**:
   - Click **Create**

### Step 4.2: Create Routes and Integrations

#### Route 1: POST /user (Create User)

1. **In UserAPI**:
   - Click **Routes** in the left menu
   - Click **Create**

2. **Configure Route**:
   ```
   Method: POST
   Path: /user
   ```
   - Click **Create**

3. **Attach Integration**:
   - Click on the route: `POST /user`
   - Click **Attach integration**
   - Click **Create and attach an integration**

4. **Integration Details**:
   ```
   Integration type: Lambda function
   Lambda function: CreateUserFunction
   ```
   - Click **Create**

#### Route 2: GET /user/{userId} (Get User)

1. **Create Route**:
   ```
   Method: GET
   Path: /user/{userId}
   ```
   - Click **Create**

2. **Attach Integration**:
   - Select the route: `GET /user/{userId}`
   - Click **Attach integration**
   - Click **Create and attach an integration**

3. **Integration Details**:
   ```
   Integration type: Lambda function
   Lambda function: GetUserFunction
   ```
   - Click **Create**

#### Route 3: DELETE /user/{userId} (Delete User)

1. **Create Route**:
   ```
   Method: DELETE
   Path: /user/{userId}
   ```
   - Click **Create**

2. **Attach Integration**:
   - Select the route: `DELETE /user/{userId}`
   - Click **Attach integration**
   - Click **Create and attach an integration**

3. **Integration Details**:
   ```
   Integration type: Lambda function
   Lambda function: DeleteUserFunction
   ```
   - Click **Create**

### Step 4.3: Get API Endpoint URL

1. Click **Stages** in the left menu
2. Click on `$default` stage
3. Copy the **Invoke URL**
   - Format: `https://xxxxxxxxxx.execute-api.region.amazonaws.com`
   - Save this URL - you'll need it for testing

---

## Part 5: Testing

### Step 5.1: Using Postman

#### Test 1: Create User

1. Open Postman
2. Create new request:
   ```
   Method: POST
   URL: https://your-api-id.execute-api.region.amazonaws.com/user
   ```

3. Set Headers:
   ```
   Content-Type: application/json
   ```

4. Set Body (Raw JSON):
   ```json
   {
     "userId": "201",
     "name": "Test User",
     "email": "test@example.com"
   }
   ```

5. Click **Send**

6. Expected Response:
   ```json
   {
     "message": "User created successfully"
   }
   ```

#### Test 2: Get User

1. New request:
   ```
   Method: GET
   URL: https://your-api-id.execute-api.region.amazonaws.com/user/201
   ```

2. Click **Send**

3. Expected Response:
   ```json
   {
     "userId": "201",
     "name": "Test User",
     "email": "test@example.com"
   }
   ```

#### Test 3: Delete User

1. New request:
   ```
   Method: DELETE
   URL: https://your-api-id.execute-api.region.amazonaws.com/user/201
   ```

2. Click **Send**

3. Expected Response:
   ```json
   {
     "message": "User 201 deleted successfully"
   }
   ```

### Step 5.2: Verify in DynamoDB

After each operation:
1. Go to DynamoDB Console
2. Navigate to UsersTable
3. Click **Explore table items**
4. Verify the data matches your expectations

---

## Troubleshooting

### Common Issues and Solutions

#### Issue 1: Lambda Function Returns 500 Error

**Possible Causes**:
- IAM role doesn't have DynamoDB permissions
- Table name mismatch
- Incorrect code

**Solution**:
1. Verify IAM role has `AmazonDynamoDBFullAccess`
2. Check that table name is exactly `UsersTable`
3. Review CloudWatch Logs:
   - Go to Lambda function
   - Click **Monitor** tab
   - Click **View logs in CloudWatch**

#### Issue 2: API Gateway Returns 403 Forbidden

**Possible Causes**:
- Lambda function not properly integrated
- Lambda resource policy missing

**Solution**:
1. Re-create the integration between API Gateway and Lambda
2. Ensure Lambda is in the same region as API Gateway

#### Issue 3: "User not found" when user exists

**Possible Causes**:
- userId mismatch (case-sensitive)
- Wrong DynamoDB table

**Solution**:
1. Verify userId in DynamoDB exactly matches the request
2. Check Lambda code is pointing to correct table

#### Issue 4: CORS Errors (in web browser)

**Solution**:
- The Lambda functions include CORS headers
- If still having issues, add CORS configuration in API Gateway:
  - Go to API → Routes
  - Configure CORS
  - Add allowed origins

### Checking CloudWatch Logs

1. Go to Lambda function
2. Click **Monitor** tab
3. Click **View logs in CloudWatch**
4. Click the latest log stream
5. Review error messages

### Testing Individual Components

**Test Lambda Separately**:
- Use Lambda's built-in test feature
- Verify function works before testing via API Gateway

**Test DynamoDB Access**:
- Try reading/writing from DynamoDB console
- Verify table exists and is accessible

---

## Cost Estimation

This lab uses AWS Free Tier eligible services:

- **DynamoDB**: First 25 GB storage free
- **Lambda**: First 1 million requests free
- **API Gateway**: First 1 million HTTP API calls free

**Expected Cost**: $0 (within Free Tier limits)

---

## Clean Up Resources

To avoid any charges after completing the lab:

1. **Delete API Gateway**:
   - Go to API Gateway
   - Select UserAPI
   - Actions → Delete

2. **Delete Lambda Functions**:
   - Go to Lambda
   - Delete all 3 functions

3. **Delete DynamoDB Table**:
   - Go to DynamoDB
   - Select UsersTable
   - Delete table

4. **Delete IAM Role**:
   - Go to IAM → Roles
   - Delete LambdaDynamoDBExecutionRole

---

## Next Steps

After completing this lab:

1. ✅ Try the REST API version for comparison
2. ✅ Add authentication using Amazon Cognito
3. ✅ Implement input validation
4. ✅ Add more CRUD operations (Update user)
5. ✅ Deploy using Infrastructure as Code (AWS SAM/CloudFormation)

---

## Additional Resources

- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
- [API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/)
- [DynamoDB Documentation](https://docs.aws.amazon.com/dynamodb/)
- [Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

---

**Questions or Issues?**

- Review CloudWatch Logs
- Check AWS Service Health Dashboard
- Contact: shankarsuthar499@gmail.com
