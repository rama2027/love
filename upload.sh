#! /bin/sh

source ./awscreds.sh
aws s3 cp $WORKSPACE\Create.yaml s3://superquality/Create.yaml
