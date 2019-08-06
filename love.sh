#!/bin/sh
sudo cp /home/ec2-user/.aws /var/lib/jenkins/workspace/test/.aws
virtualenv -p /usr/bin/python3 python3
pip3 install boto3
python3 ram.py
