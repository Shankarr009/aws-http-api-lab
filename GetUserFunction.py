import json
import boto3
from boto3.dynamodb.conditions import Key

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UsersTable')

def lambda_handler(event, context):
    """
    Lambda function to get a user from DynamoDB by userId
    
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
        
        # Get item from DynamoDB
        response = table.get_item(
            Key={
                'userId': user_id
            }
        )
        
        # Check if item exists
        if 'Item' in response:
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps(response['Item'])
            }
        else:
            return {
                'statusCode': 404,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({
                    'message': 'User not found'
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
