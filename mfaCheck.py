import json

#AWS SDK for Python
import boto3 

#client for IAM service
client=boto3.client('iam') 

def lambda_handler(event, context):
    #retrieve all IAM users
    response = client.list_users() 
    
    #loop through users to determine who has MFA
    for user in response['Users']:
        userMFA = client.list_mfa_devices(UserName=user['UserName'])
        if len(userMFA['MFADevices']) == 0 :
            print("This user doesn't have MFA activated: ", user['UserName'])
        else:
            print("This user has activated MFA: ", user['UserName'])
    
    return {
        'statusCode': 200,
        'body': json.dumps('Successful MFA check')
    }
