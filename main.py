import os
from google.cloud import storage


import boto3
import os

# Replace these with your own AWS credentials and S3 bucket name
aws_access_key_id = 'AKIA4EJGH4Q2HOJ4DYCU'
aws_secret_access_key = 'K+hX1sq+AFut9vGJ1gzuDGszATAtvjV2qbFWQneC'
bucket_name = 'my-space-app-hackathon'
dataset_file_path = 'C:\dev\Projects\NASASpaceAppHackathon\NASA_SpaceAppChallenge\dummy_data\CPIForecast.csv'
s3_object_key = 'CPIForecast.csv'  # The name you want to give to the dataset in S3



# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Upload the dataset file to S3
try:
    s3.upload_file(dataset_file_path, bucket_name, s3_object_key)
    print(f"Upload successful: {dataset_file_path} to s3://{bucket_name}/{s3_object_key}")
except Exception as e:
    print(f"Upload failed: {str(e)}")
