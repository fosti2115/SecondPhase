import boto3
from botocore.exceptions import NoCredentialsError

# AWS credentials
AWS_KEY_ID = "AKIAJ6AS7R7DFJ4RHTAQ"
AWS_SECRET_ACCESS_KEY = "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"

# Function to list S3 buckets using AWS credentials
def list_s3_buckets(aws_key_id, aws_secret_access_key):
    try:
        # Create a session using the provided AWS credentials
        session = boto3.Session(
            aws_access_key_id=aws_key_id,
            aws_secret_access_key=aws_secret_access_key
        )

        # Create an S3 client
        s3_client = session.client('s3')

        # List the S3 buckets
        response = s3_client.list_buckets()
        
        print("Buckets:")
        for bucket in response['Buckets']:
            print(f"  {bucket['Name']}")

    except NoCredentialsError:
        print("Credentials not available")

# Call the function with the provided AWS credentials
list_s3_buckets(AWS_KEY_ID, AWS_SECRET_ACCESS_KEY)
