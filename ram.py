import boto3
import os
client = boto3.client(
    'ec2',
    aws_access_key_id=$AWS_ACCESS_KEY_ID,
    aws_secret_access_key=$AWS_SECRET_ACCESS_KEY,
)
response = ec2.describe_instances()
print(response)
