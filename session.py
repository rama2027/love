import boto3
import os

sts = boto3.client('sts')

assumed_role_object= sts.assume_role(
    RoleArn=os.environ['IAM_ROLE'],
    RoleSessionName="AssumeRoleSession"
)
credentials = assumed_role_object['Credentials']
test = credentials['AccessKeyId']
print(test)
resource = boto3.resource(
    'ec2',
    AWS_ACCESS_KEY_ID=credentials['AccessKeyId'],
    AWS_SECRET_ACCESS_KEY=credentials['SecretAccessKey'],
    AWS_SESSION_TOKEN=credentials['SessionToken'],
    region_name = 'eu-west-1'
)
response = resource.describe_instances()
print(response)
