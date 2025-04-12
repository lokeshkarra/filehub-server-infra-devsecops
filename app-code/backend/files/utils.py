import boto3
from botocore.exceptions import NoCredentialsError

def generate_presigned_url(bucket_name, object_key, expiration=3600):
    """
    Generate a presigned URL to access a private S3 object.
    :param bucket_name: Name of the S3 bucket.
    :param object_key: Key (path) of the object in the bucket.
    :param expiration: Time in seconds for the presigned URL to remain valid.
    :return: Presigned URL as a string or None if an error occurs.
    """
    s3_client = boto3.client('s3')
    try:
        url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': object_key},
            ExpiresIn=expiration
        )
        return url
    except NoCredentialsError:
        return None