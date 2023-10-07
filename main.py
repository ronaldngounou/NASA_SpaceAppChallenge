import os
from google.cloud import storage

# Set the path to your JSON key file (replace with the actual path)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\dev\Projects\NASASpaceAppHackathon\myspaceapp-401320-f3e0c5007d1a.json"

# Initialize a client
client = storage.Client()

# Set your bucket name
bucket_name = "myspaceapp"

# Specify the local file you want to upload
local_file_path = "C:\dev\Projects\NASASpaceAppHackathon\NASA_SpaceAppChallenge\dummy_data\CPIForecast.csv"

# Specify the destination object name (key) in the bucket
destination_blob_name = "destination/CPIForecast.csv"

# Get a reference to the bucket
bucket = client.get_bucket(bucket_name)

# Upload the file to Google Cloud Storage
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(local_file_path)

print(f"File {local_file_path} uploaded to {bucket_name}/{destination_blob_name}")
