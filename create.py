import boto3
import os

ec2 = boto3.resource('ec2',region_name='eu-west-1',
    aws_access_key_id=AKIAVO4RZPOTNPZMVD37,
    aws_secret_access_key=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)

response = ec2.create_instances(
     ImageId='ami-0bbc25e23a7640b9b',
     MinCount=1,
     MaxCount=2,
     InstanceType='t2.micro',
     KeyName='test'
 )
print(response)
