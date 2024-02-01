import json
from functions import image


def handler(event):
    file_name = event['queryStringParameters']['file_name']
    response = image.get_upload_url(file_name)

    return {"statusCode": 200, "body": json.dumps(response)}
