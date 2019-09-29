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

os.environ['AWS_ACCESS_KEY_ID'] = newsession_key
os.environ['AWS_SECRET_ACCESS_KEY'] = newsession_key
os.environ['AWS_SESSION_TOKEN'] = newsession_token

print (os.environ['AWS_ACCESS_KEY_ID'])

file = open('awscreds.sh', 'w')
file .write('export AWS_ACCESS_KEY_ID=' + newsession_id + '\n')
file .write('export AWS_SECRET_ACCESS_KEY=' + newsession_key + '\n')
file .write('export AWS_SESSION_TOKEN=' + newsession_token + '\n')
