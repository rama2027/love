import boto3
import os

sts = boto3.client('sts')

assumed_role_object= sts.assume_role(
    RoleArn=os.environ['IAM_ROLE'],
    RoleSessionName="AssumeRoleSession1"
)
credentials=assumed_role_object['Credentials']
resource = boto3.resource(
    'ec2',
    aws_access_key_id=credentials['AccessKeyId'],
    aws_secret_access_key=credentials['SecretAccessKey'],
    aws_session_token=credentials['SessionToken']
    region_name = 'eu-west-1'
)
response = resource.describe_instances()
print(response)
