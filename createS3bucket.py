import boto3

sess= boto3.Session(region_name='us-east-1')
s3client = sess.client('s3')
bucket_name='big-thing-happen-big1'
s3_location={
    'LocationConstraint': 'us-east-1'
}
s3client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=s3_location)
