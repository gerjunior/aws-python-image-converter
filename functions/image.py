import os
import boto3

BUCKET = os.environ['BUCKET']

s3 = boto3.client('s3')


def get_upload_url(key):
    response = s3.generate_presigned_post(
        BUCKET,
        key,
    )

    return response


def get_download_url(key):
    response = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': BUCKET, 'Key': key},
    )

    return response


def download_file(key):
    path = f'/tmp/{key}'
    s3.download_file(BUCKET, key, path)
    return path


def put_object(key, body):
    response = s3.put_object(
        Bucket=BUCKET,
        Key=key,
        Body=body
    )

    return response
