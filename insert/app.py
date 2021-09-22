import json
import uuid
import boto3


def lambda_handler(event, context):
    client = boto3.client('dynamodb')
    body = event['body']
    if not body:
        return {
            "statusCode": 200,
            "body": json.dumps({
                "error": "body required"
            })
        }
    body = json.loads(body) 
    if not body['title'] or not body['description']:
        return {
            "statusCode": 200,
            "body": json.dumps({
                "error": "title and description is required"
            })
        }
    try:
        uid = str(uuid.uuid4()).replace('-', '')
        print(uid)
        response = client.put_item(
            TableName='itable',
            Item={
                'id': {
                    'S': uid
                },
                'title': {
                    'S': body['title'],
                },
                'description': {
                    'S': body['description']
                }
            })
    except Exception as e:
        return {
            "statusCode": 200,
            "body": json.dumps({
                "error": e.__str__()
            })
        }

    return {
        "statusCode": 200,
        "body": json.dumps({
            "success": True,
            "response": response
        })
    }
