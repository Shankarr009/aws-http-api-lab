# Quick Start Guide

Get your AWS HTTP API Lab up and running in 30 minutes!

## 🚀 Prerequisites Checklist

Before you begin, make sure you have:

- [ ] AWS Account (Free Tier eligible)
- [ ] AWS Console access
- [ ] Postman installed (or cURL)
- [ ] 30-45 minutes of time

## ⚡ Quick Setup (5 Steps)

### Step 1: Create DynamoDB Table (5 min)

1. Open AWS Console → DynamoDB
2. Click **Create table**
3. Settings:
   - Table name: `UsersTable`
   - Partition key: `userId` (String)
4. Click **Create table**

✅ **Done!** Your database is ready.

---

### Step 2: Create IAM Role (3 min)

1. Open AWS Console → IAM → Roles
2. Click **Create role**
3. Select: AWS service → Lambda
4. Add policy: `AmazonDynamoDBFullAccess`
5. Name: `LambdaDynamoDBExecutionRole`
6. Click **Create role**

✅ **Done!** Lambda now has database access.

---

### Step 3: Create Lambda Functions (10 min)

Create 3 Lambda functions with these settings:

**Common Settings (use for all 3)**:
- Runtime: Python 3.12
- Existing role: `LambdaDynamoDBExecutionRole`

#### Function 1: CreateUserFunction
```python
# Copy code from: lambda-functions/CreateUserFunction.py
# Paste in Lambda console → Deploy
```

#### Function 2: GetUserFunction
```python
# Copy code from: lambda-functions/GetUserFunction.py
# Paste in Lambda console → Deploy
```

#### Function 3: DeleteUserFunction
```python
# Copy code from: lambda-functions/DeleteUserFunction.py
# Paste in Lambda console → Deploy
```

✅ **Done!** Your API logic is ready.

---

### Step 4: Create API Gateway (5 min)

1. Open AWS Console → API Gateway
2. Click **Create API** → HTTP API → Build
3. API name: `UserAPI` → Create

**Add Routes**:

| Method | Path | Lambda Function |
|--------|------|----------------|
| POST | /user | CreateUserFunction |
| GET | /user/{userId} | GetUserFunction |
| DELETE | /user/{userId} | DeleteUserFunction |

For each route:
- Click **Create** → Select method and path
- Click **Attach integration** → Lambda function
- Select the corresponding function

4. Go to **Stages** → Copy the **Invoke URL**

✅ **Done!** Your API is live!

---

### Step 5: Test Your API (5 min)

**Get Your API URL**:
```
Go to API Gateway → UserAPI → Stages → $default
Copy the Invoke URL
```

**Test in Postman**:

1. **Create User**:
   ```
   POST https://your-api-id.execute-api.region.amazonaws.com/user
   
   Body (JSON):
   {
     "userId": "101",
     "name": "Your Name",
     "email": "your@email.com"
   }
   ```

2. **Get User**:
   ```
   GET https://your-api-id.execute-api.region.amazonaws.com/user/101
   ```

3. **Delete User**:
   ```
   DELETE https://your-api-id.execute-api.region.amazonaws.com/user/101
   ```

✅ **Done!** You've built a complete serverless API!

---

## 🎯 What You've Built

```
Mobile/Web App
      ↓
  API Gateway (HTTP API)
      ↓
  Lambda Functions
      ↓
  DynamoDB
```

You now have:
- ✅ Serverless REST API
- ✅ NoSQL database
- ✅ Automatic scaling
- ✅ Pay-per-use pricing
- ✅ Production-ready architecture

---

## 📱 Test with cURL (Alternative to Postman)

```bash
# Replace YOUR_API_URL with your actual API Gateway URL

# Create User
curl -X POST YOUR_API_URL/user \
  -H "Content-Type: application/json" \
  -d '{"userId":"101","name":"Test User","email":"test@example.com"}'

# Get User
curl YOUR_API_URL/user/101

# Delete User
curl -X DELETE YOUR_API_URL/user/101
```

---

## 🔍 Verify Everything Works

1. **Check DynamoDB**:
   - Go to DynamoDB → UsersTable → Explore items
   - You should see your created users

2. **Check Lambda Logs**:
   - Go to Lambda → Function → Monitor → CloudWatch Logs
   - Verify no errors

3. **Test All Operations**:
   - Create a user ✅
   - Get the user ✅
   - Delete the user ✅

---

## 🐛 Common Issues

### Issue: "User not created"
**Solution**: Check Lambda function logs in CloudWatch

### Issue: "403 Forbidden"
**Solution**: Verify API Gateway integration with Lambda

### Issue: "Internal Server Error"
**Solution**: Check IAM role has DynamoDB permissions

### Issue: "Table does not exist"
**Solution**: Verify table name is exactly `UsersTable`

---

## 💡 Next Steps

Now that your API is working:

1. ✅ Add more users with different IDs
2. ✅ Try invalid requests (missing fields)
3. ✅ Check CloudWatch for logs
4. ✅ Add an UPDATE endpoint (optional challenge!)
5. ✅ Deploy with AWS SAM or CloudFormation

---

## 📚 Full Documentation

For detailed information:
- [Complete Setup Guide](setup-guide.md)
- [API Documentation](api-documentation.md)
- [Architecture Diagram](../assets/architecture-diagram.md)
- [Troubleshooting](setup-guide.md#troubleshooting)

---

## 🎉 Congratulations!

You've successfully built a serverless REST API on AWS!

**What you learned**:
- Creating DynamoDB tables
- Writing Lambda functions
- Setting up API Gateway
- Testing APIs with Postman
- AWS security with IAM roles

**Cost**: $0 (within Free Tier)

---

## 🧹 Clean Up (When Done)

To avoid any charges:

1. Delete API Gateway: `UserAPI`
2. Delete Lambda functions: All 3
3. Delete DynamoDB table: `UsersTable`
4. Delete IAM role: `LambdaDynamoDBExecutionRole`

---

## 📞 Need Help?

- Review [Setup Guide](setup-guide.md)
- Check [Troubleshooting](setup-guide.md#troubleshooting)
- Email: shankarsuthar499@gmail.com

---

⭐ **Enjoy building with AWS!**
