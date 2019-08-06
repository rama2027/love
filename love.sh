#!/bin/sh
mkdir ram2
cd ram2
git clone https://github.com/rama2027/love.git
sudo cp -r /home/ec2-user/.aws /var/lib/jenkins/workspace/test/ram2/.aws
sudo pip3 install virtualenv
virtualenv ram2
source ram/bin/activate
pip3 install boto3
python3 ram.py
