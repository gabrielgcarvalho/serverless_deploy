import boto3
import json


def lambda_handler(event, context):
    client = boto3.client('s3')

    for record in event['Records']:
        eventName = record['eventName']
        if eventName == 'INSERT':
            data = json.dumps(record['dynamodb']['NewImage']) 
            data_id = record['dynamodb']['Keys']['id']['S']
            response = client.put_object(
                        ACL='public-read',
                        Body= data,
                        Bucket='serverless-s3b',
                        Key='txt/'+ data_id + '.txt')
            print("image: " + json.dumps(record['dynamodb']))
            print(response)
        print(eventName)
    

    
