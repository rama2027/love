#!/bin/sh
mkdir ram3
cd ram3
sudo git clone https://github.com/rama2027/love.git
sudo cp -r /home/ec2-user/.aws /var/lib/jenkins/workspace/test/ram3/.aws
ls
sudo pip3 install virtualenv
virtualenv ram3
source ram2/bin/activate
pip3 install boto3
python3 ram.py
