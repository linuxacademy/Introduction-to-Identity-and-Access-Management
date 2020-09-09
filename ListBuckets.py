import json

#AWS SDK for Python
import boto3 

#client for S3
s3 = boto3.client('s3')

def lambda_handler(event, context):
    
    # Retrieve the list of existing buckets
    response = s3.list_buckets()

    # Print existing buckets
    for bucket in response['Buckets']:
        print(bucket["Name"])
    
    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }