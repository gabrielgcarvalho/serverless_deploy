import boto3


def lambda_handler(event, context):
    client = boto3.client('dynamodb')
    for record in event['Records']:
        s3_key =  str(record['s3']['object']['key'])
        s3_key = s3_key.replace('txt/', '').replace('.txt', '')
        response = client.delete_item(
                            TableName='itable',
                            Key={
                                'id': {
                                 'S': s3_key
                            }},)
        print(s3_key)
        print(response)