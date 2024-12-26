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
