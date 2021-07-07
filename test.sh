#!/bin/sh
pwd
source ./awscreds.sh
pwd
python --version
printenv
aws ec2 describe-instances --region eu-west-1
ls
printenv
