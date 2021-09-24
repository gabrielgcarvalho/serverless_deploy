import boto3
import json
import os

from botocore.retries import bucket


def lambda_handler(event, context):
    client = boto3.client('s3')
    bucket_name = os.environ['BUCKET_NAME']
    for record in event['Records']:
        eventName = record['eventName']
        if eventName == 'INSERT':
            data = json.dumps(record['dynamodb']['NewImage']) 
            data_id = record['dynamodb']['Keys']['id']['S']
            response = client.put_object(
                        ACL='public-read',
                        Body= data,
                        Bucket=bucket_name,
                        Key='txt/'+ data_id + '.txt')
            print("image: " + json.dumps(record['dynamodb']))
            print(response)
        print(eventName)
    

    
