import os
import boto3

BUCKET = os.environ['BUCKET']

s3 = boto3.client('s3')


def upload(key):
    response = s3.generate_presigned_post(
        BUCKET,
        key,
    )

    return response


def download(key):
    response = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': BUCKET, 'Key': key},
    )

    return response
