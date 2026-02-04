import json
import boto3

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UsersTable')

def lambda_handler(event, context):
    """
    Lambda function to delete a user from DynamoDB by userId
    
    Expected event structure:
    {
        "pathParameters": {
            "userId": "101"
        }
    }
    """
    try:
        # Extract userId from path parameters
        user_id = event['pathParameters']['userId']
        
        # Delete item from DynamoDB
        response = table.delete_item(
            Key={
                'userId': user_id
            }
        )
        
        # Return success response
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'message': f'User {user_id} deleted successfully'
            })
        }
        
    except KeyError as e:
        # Handle missing path parameters
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'error': f'Missing required parameter: {str(e)}'
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
