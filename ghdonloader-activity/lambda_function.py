import json
from downloader import download_file
def lambda_handler(event, context):
    res = download_file("2021-01-20-0.json.gz")
    return {
        'statusCode': res.status_code ,
        'body': json.dumps('Hello from Lambda! From Zipped file')
    }