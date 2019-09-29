#!/bin/sh
python --version
printenv
aws ec2 describe-instances --region eu-west-1
ls
printenv
