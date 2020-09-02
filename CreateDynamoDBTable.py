import json

#AWS SDK for Python
import boto3 

#client for DynamoDB
dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    
    #create table
    table = dynamodb.create_table(
        TableName='Courses',
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'name',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'name',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }