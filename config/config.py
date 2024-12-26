from dotenv import load_dotenv

import os

load_dotenv()

def str_to_bool(value):
    return value.lower() in ("true", "1", "t", "yes")

minio_config = {
    'AWS_ENDPOINT_URL': os.getenv("AWS_ENDPOINT_URL"),
    'AWS_ACCESS_KEY': os.getenv("AWS_ACCESS_KEY"),
    'AWS_SECRET_KEY': os.getenv("AWS_SECRET_KEY"),
    'AWS_REGION_NAME': os.getenv("AWS_REGION_NAME"),
    'AWS_BUCkET': os.getenv("AWS_BUCkET"),
    'AWS_USE_SSL': str_to_bool(os.getenv("AWS_USE_SSL", "false"))
}

# minio_config = {
#     'AWS_ENDPOINT_URL': 'http://79.127.87.84:50000',
#     'AWS_ACCESS_KEY': 'spGDo12SwuoBh3pVv7ji',
#     'AWS_SECRET_KEY': 'qah56VYunTMo6LIoFQGEJzEDvqyghiCNE5Ovr9kW',
#     'AWS_REGION_NAME': 'us-east-1',
#     'AWS_BUCkET': 'backup',
#     'AWS_USE_SSL': False
# }
