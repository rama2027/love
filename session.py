import boto3
import os

sts = boto3.client('sts')

assumed_role_object = sts.assume_role(
    RoleArn=os.environ['IAM_ROLE'],
    RoleSessionName="love"
)
credentials = assumed_role_object['Credentials']
resource = boto3.resource('ec2',region_name = 'eu-west-1')
response = resource.describe_instances()
print(response)
