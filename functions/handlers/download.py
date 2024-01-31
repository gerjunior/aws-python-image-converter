from functions import image


def handler(event, _context):
    file_name = event['pathParameters']['file_name']

    link = image.download(file_name)

    return {"statusCode": 200, "body": link, 'headers': {
        'Content-Type': 'image/jpeg',
    }}
