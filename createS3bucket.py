import boto3
import os
os.environ['AWS_PROFILE'] = default
os.environ['AWS_DEFAULT_REGION'] = us-east-1
sess= boto3.Session(region_name='us-east-1')
s3client = sess.client('s3')
# s3 = boto3.resource('s3',
#          aws_access_key_id=ACCESS_ID,
#          aws_secret_access_key= ACCESS_KEY)

bucket_name='prudential-s3'
s3_location={
    'LocationConstraint': 'us-east-1'
}

s3client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=s3_location)

# import boto3
# sess= boto3.Session(region_name='us-east-2')
# s3client = sess.client('s3')
# bucket_name='prudential-s3'
# s3_location={
#     'LocationConstraint': 'us-east-2'
# }
# s3client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=s3_location)
