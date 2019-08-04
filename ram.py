import boto3
ec2 = boto3.resource('ec2',region_name = 'eu-west-1')
instance = ec2.create_instances(
    ImageId = 'ami-0bbc25e23a7640b9b',
    MinCount = 1,
    MaxCount = 1,
    InstanceType = 't2.micro',
    KeyName = 'test')
print (instance[0].id)
