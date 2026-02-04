# Git Setup Instructions

Follow these steps to push this project to your GitHub repository.

## Step 1: Initialize Git Repository

```bash
cd aws-http-api-lab
git init
```

## Step 2: Add All Files

```bash
git add .
```

## Step 3: Create Initial Commit

```bash
git commit -m "Initial commit: AWS HTTP API Lab with complete documentation"
```

## Step 4: Create GitHub Repository

1. Go to [GitHub](https://github.com)
2. Click the **+** icon → **New repository**
3. Repository name: `aws-http-api-lab`
4. Description: `A hands-on lab for building serverless REST APIs with AWS API Gateway, Lambda, and DynamoDB`
5. Choose **Public** or **Private**
6. **Do NOT** initialize with README (we already have one)
7. Click **Create repository**

## Step 5: Connect to GitHub Repository

```bash
git remote add origin https://github.com/shankarr009/aws-http-api-lab.git
git branch -M main
```

## Step 6: Push to GitHub

```bash
git push -u origin main
```

## Step 7: Verify

1. Go to https://github.com/shankarr009/aws-http-api-lab
2. You should see all your files
3. README.md will display on the repository homepage

## Alternative: Using GitHub CLI

If you have [GitHub CLI](https://cli.github.com/) installed:

```bash
# Initialize repository
cd aws-http-api-lab
git init
git add .
git commit -m "Initial commit: AWS HTTP API Lab"

# Create repository and push
gh repo create aws-http-api-lab --public --source=. --remote=origin --push
```

## Adding Repository Topics (Optional)

After pushing, add topics to your repository:

1. Go to your repository on GitHub
2. Click the gear icon next to "About"
3. Add topics:
   - aws
   - lambda
   - api-gateway
   - dynamodb
   - serverless
   - python
   - rest-api
   - aws-sdk
   - http-api
   - boto3

## Repository Settings (Recommended)

### Enable GitHub Pages (Optional)

1. Go to Settings → Pages
2. Source: Deploy from branch
3. Branch: main / docs
4. This will host your documentation

### Add Repository Description

```
A hands-on lab for building serverless REST APIs with AWS API Gateway (HTTP API), Lambda functions, and DynamoDB. Complete with step-by-step setup guide, Lambda code, and Postman collection.
```

### Add Repository Website (Optional)

If you deployed your API:
```
https://your-api-id.execute-api.region.amazonaws.com
```

## Keeping Repository Updated

After making changes:

```bash
git add .
git commit -m "Description of changes"
git push origin main
```

## Branching Strategy (Optional)

For development:

```bash
# Create and switch to develop branch
git checkout -b develop

# Make changes, then
git add .
git commit -m "Your changes"
git push origin develop

# Create pull request on GitHub
# After review, merge to main
```

## Common Git Commands

```bash
# Check status
git status

# View commit history
git log --oneline

# Create new branch
git checkout -b feature/new-feature

# Switch branches
git checkout main

# Pull latest changes
git pull origin main

# View remote URL
git remote -v
```

## Troubleshooting

### Error: "remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/shankarr009/aws-http-api-lab.git
```

### Error: "failed to push"
```bash
# Pull first if remote has changes
git pull origin main --rebase
git push origin main
```

### Error: "fatal: not a git repository"
```bash
# Make sure you're in the project directory
cd aws-http-api-lab
git init
```

## Next Steps

After pushing to GitHub:

1. ✅ Add repository description and topics
2. ✅ Enable GitHub Actions (CI/CD pipeline included)
3. ✅ Create issues for future enhancements
4. ✅ Add collaborators if working with a team
5. ✅ Share your repository!

---

**Your repository will be live at:**
https://github.com/shankarr009/aws-http-api-lab

---

🎉 **Congratulations!** Your AWS HTTP API Lab is now on GitHub!
