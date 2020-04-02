
import boto3
import logging
from botocore.exceptions import ClientError
import uuid 


def create_bucket(bucket_name):
        
    bucket_name = create_bucket_name(bucket_prefix)
    session = boto3.session.Session()
    current_region = session.region_name


    s3 = boto3.client('s3')
    try:
        s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint':current_region})
    except ClientError as e:
        logging.error(e)
        return False
    return True


def create_bucket_name(bucket_prefix):
    return '-'.join([bucket_prefix, str(uuid.uuid4())])
    
    
bucket_prefix = input('Please input bucket prefix: ')
create_bucket(bucket_prefix)