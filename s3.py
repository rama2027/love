import boto3
import os

sts = boto3.client('sts')

assumed_role_object = sts.assume_role(
    RoleArn=os.environ['IAM_ROLE'],
    RoleSessionName="love"
)

newsession_id = assumed_role_object["Credentials"]["AccessKeyId"]
newsession_key = assumed_role_object["Credentials"]["SecretAccessKey"]
newsession_token = assumed_role_object["Credentials"]["SessionToken"]

ec2 = boto3.client('ec2',region_name='us-east-1',
    aws_access_key_id=newsession_id,
    aws_secret_access_key=newsession_key,
    aws_session_token=newsession_token)

response = ec2.create_instances(
     ImageId='ami-00b6a8a2bd28daf19',
     MinCount=1,
     MaxCount=2,
     InstanceType='t2.micro',
     KeyName='ec2-keypair'
 )
print(response)
