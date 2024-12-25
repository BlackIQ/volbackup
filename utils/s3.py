import boto3
from botocore.exceptions import NoCredentialsError, ClientError

from config.config import minio_config

s3 = boto3.client(
    's3',
    endpoint_url=minio_config['AWS_ENDPOINT_URL'],
    aws_access_key_id=minio_config['AWS_ACCESS_KEY'],
    aws_secret_access_key=minio_config['AWS_SECRET_KEY'],
    region_name=minio_config['AWS_REGION_NAME'],
    use_ssl=minio_config['AWS_USE_SSL']
)

def upload_file(file_name, object_name):
    try:
        s3.upload_file(file_name, minio_config['AWS_BUCkET'], object_name)
        
        print(f"File {file_name} uploaded to {minio_config['AWS_BUCkET']}/{object_name}")
    except FileNotFoundError:
        print(f"File {file_name} not found")
    except NoCredentialsError:
        print("Credentials not available")
    except ClientError as e:
        print(f"Error: {e}")