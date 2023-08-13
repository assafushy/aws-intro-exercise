# S3 Intro

## Create an S3 Bucket using the AWS Console

## Create an S3 Bucket using the AWS CLI

```bash
aws s3 mb --bucket my-bucket
```

## Hosting a Static Website on S3

Good docs can be found -
https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html

## Accessing S3 from an ECS Task

Create a task definition with these settings:

1. container image - https://hub.docker.com/r/amazon/aws-cli
2. Role - s3-access-role
