#!/bin/bash
ACCOUNT_ID=$(aws sts get-caller-identity --query 'Account' --output text)

aws s3 mb s3://terraform-backend-bucket-${ACCOUNT_ID}


# need versioning
#aws s3api put-bucket-versioning --bucket s3://terraform-backend-bucket-${ACCOUNT_ID} --versioning-configuration Status=Enabled

# need encryption

# block public access to bucket

# create ddb table