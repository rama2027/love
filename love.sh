#!/bin/sh
sudo cp -r /home/ec2-user/.aws /var/lib/jenkins/workspace/test/
python3 ram.py
