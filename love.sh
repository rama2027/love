#!/bin/sh
# This is a comment!
yum install python python-devel python-pip
python-pip install boto
python -c "import boto; print boto.Version"
