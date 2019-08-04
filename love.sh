#!/bin/sh
git clone https://github.com/rama2027/love
virtualenv -p /usr/bin/python3 python3
pip3 install boto3
sudo cp /home/ec2-user/.aws /var/lib/jenkins/workspace/test/.aws
python3 ram.py
