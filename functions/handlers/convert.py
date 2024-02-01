import os.path
from pathlib import Path

from PIL import Image
from functions import image

thumbnail_size = (128, 128)


def handler(event, _context):
    object_key = event['Records'][0]['s3']['object']['key']

    file_path = image.download_file(object_key)
    thumbnail_file_path = Path('/tmp', file_path)

    with Image.open(file_path) as im:
        im.thumbnail(thumbnail_size)
        im.save(thumbnail_file_path)

    thumbnail_object_key = f"thumbnails/{object_key}"
    image.put_object(thumbnail_object_key, open(thumbnail_file_path, 'rb'))

    return {"statusCode": 200, "body": "Image converted and uploaded to S3"}
