import boto3

def create_s3_bucket(bucket_name, region='us-west-2'):
    try:
        # Create an S3 client
        s3 = boto3.client('s3', region_name=region)

        # Create the S3 bucket
        s3.create_bucket(Bucket=bucket_name)

        print(f"Bucket '{bucket_name}' created successfully!")
    except Exception as e:
        print(f"Error creating bucket: {e}")

if __name__ == "__main__":
    # Replace 'your-bucket-name' with your desired bucket name
    bucket_name = 'your-bucket-name'
    create_s3_bucket(bucket_name)
