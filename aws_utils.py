# aws_utils.py

import boto3
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, REGION

def create_s3_bucket(bucket_name, region=REGION):
    try:
        #....................Create an S3 client.....................
        s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
                           aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                           region_name=region)

        # .................Create the S3 bucket......................
        s3.create_bucket(Bucket=bucket_name)

        print(f"Bucket '{bucket_name}' created successfully!")
    except Exception as e:
        print(f"Error creating bucket: {e}")

def upload_file_to_s3(file_path, bucket_name, region=REGION):
    try:
        # ....................Create an S3 client ..........................
        s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
                           aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                           region_name=region)

        # ..........................Upload the file to S3...................
        s3.upload_file(file_path, bucket_name, file_path.split('/')[-1])

        print(f"File '{file_path}' uploaded to S3 successfully!")
    except Exception as e:
        print(f"Error uploading file: {e}")
