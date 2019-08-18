import boto3
import os
import sys

sts = boto3.client('sts')

assumed_role_object = sts.assume_role(
    RoleArn=os.environ['IAM_ROLE'],
    RoleSessionName="love"
)

newsession_id = assumed_role_object["Credentials"]["AccessKeyId"]
newsession_key = assumed_role_object["Credentials"]["SecretAccessKey"]
newsession_token = assumed_role_object["Credentials"]["SessionToken"]

s3 = boto3.client('s3',
    aws_access_key_id=newsession_id,
    aws_secret_access_key=newsession_key,
    aws_session_token=newsession_token)

Bucketname=os.environ['Bucket']
file="test.json"
lov = s3.create_bucket(Bucket=os.environ['Bucket'],CreateBucketConfiguration={'LocationConstraint': 'os.environ['Location']'})
s3 = boto3.resource('s3')
bucket = s3.Bucket(os.environ['Bucket'])
bucket.upload_file("test.json", file)
location = boto3.client('s3').get_bucket_location(Bucketname=os.environ['Bucket'])['LocationConstraint': 'os.environ['Location']']
url = "https://s3-%s.amazonaws.com/%s/%s" % (location, bucket_name, key)
print(url)



