import boto3

sess= boto3.Session(region_name='us-east-2')
s3client = sess.client('s3')
bucket_name='big-thing-happen-big1'
s3_location={
    'LocationConstraint': 'us-east-2'
}
try:
    s3client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=s3_location)
except: # you can catch the specific error that boto3 throws when it already exists, for now lets simply do nothing.
  pass
