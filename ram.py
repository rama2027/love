import boto3
import os
client = boto3.client(
    'ec2',
    aws_access_key_id="AKIAVO4RZPOTCNCUGBF4",
    aws_secret_access_key="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",
    region_name = 'eu-west-1'
)
response = client.describe_instances()
print(response)
