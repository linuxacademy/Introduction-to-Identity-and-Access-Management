import json

#AWS SDK for Python
import boto3 

#client for DynamoDB
dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    #retrieve item from table
    dynamodb.get_item(TableName='courses', Key={'id':{'S':'1'}})
    
    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }