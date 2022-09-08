import boto3


sess= boto3.Session(region_name='us-east-2')


# s3client = sess.client('s3')
s3 = boto3.resource('s3',
         aws_access_key_id=ACCESS_ID,
         aws_secret_access_key= ACCESS_KEY)

bucket_name='prudential-s3'
s3_location={
    'LocationConstraint': 'us-east-2'
}

s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=s3_location)
