#!/bin/sh
git clone https://github.com/rama2027/love
virtualenv -p /usr/bin/python3 python3
pip3 install boto3
python3 ram.py
