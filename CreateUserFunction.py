import json
import boto3

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UsersTable')

def lambda_handler(event, context):
    """
    Lambda function to create a new user in DynamoDB
    
    Expected event structure:
    {
        "body": "{\"userId\": \"101\", \"name\": \"John Doe\", \"email\": \"john@example.com\"}"
    }
    """
    try:
        # Parse the request body
        body = json.loads(event['body'])
        
        # Extract user details
        user_id = body['userId']
        name = body['name']
        email = body['email']
        
        # Insert item into DynamoDB
        table.put_item(
            Item={
                'userId': user_id,
                'name': name,
                'email': email
            }
        )
        
        # Return success response
        return {
            'statusCode': 201,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'message': 'User created successfully'
            })
        }
        
    except KeyError as e:
        # Handle missing required fields
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'error': f'Missing required field: {str(e)}'
            })
        }
        
    except Exception as e:
        # Handle any other errors
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'error': str(e)
            })
        }
