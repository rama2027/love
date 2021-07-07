#!/bin/sh

source ./awscreds.sh
aws s3 mb s3://$BUCKETNAME --region $REGION
aws s3 ls
