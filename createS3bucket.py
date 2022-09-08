import boto3


sess= boto3.Session(region_name='us-east-2')


s3client = sess.client('s3')

bucket_name='prudential-s3'
s3_location={
    'LocationConstraint': 'us-east-2'
}

s3client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=s3_location)
