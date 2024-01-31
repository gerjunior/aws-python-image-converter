
# s3 event notification handler
def handler(event, context):
    # object_key = event['Records'][0]['s3']['object']['key']

    # convert the image
    # upload the image to s3

    return {"statusCode": 200, "body": "Image converted and uploaded to S3"}
