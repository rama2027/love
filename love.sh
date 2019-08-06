#!/bin/sh
sudo cp -r /home/ec2-user/.aws /var/lib/jenkins/workspace/test/.aws
pip3 install virtualenv
virtualenv ram
source ram/bin/activate
pip3 install boto3
python3 ram.py
