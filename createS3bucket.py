import boto3
import os
from dotenv import load_dotenv
load_dotenv()


ACCESS_KEY=os.getenv('ACCESS_KEY')
SECRET_KEY=os.getenv('SECRET_KEY')

print(ACCESS_KEY)

sess= boto3.Session(aws_access_key_id=ACCESS_KEY,
                    aws_secret_access_key=SECRET_KEY,
                    region_name='us-east-2')


s3client = sess.client('s3')

bucket_name='prudential1-s3'
s3_location={
    'LocationConstraint': 'us-east-2'
}

s3client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=s3_location)


# import boto3
# import os
# os.environ['AWS_PROFILE'] = 'default'
# os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'
# sess= boto3.Session(region_name='us-east-1')
# s3client = sess.client('s3')
# # s3 = boto3.resource('s3',
# #          aws_access_key_id=ACCESS_ID,
# #          aws_secret_access_key= ACCESS_KEY)

# bucket_name='prudential-s3'
# s3_location={
#     'LocationConstraint': 'us-east-1'
# }

# s3client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=s3_location)

# # import boto3
# sess= boto3.Session(region_name='us-east-2')
# s3client = sess.client('s3')
# bucket_name='prudential-s3'
# s3_location={
#     'LocationConstraint': 'us-east-2'
# }
# s3client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=s3_location)
