#!/bin/sh

aws s3 create-bucket --bucket $BUCKETNAME --region $REGION
aws s3 list
