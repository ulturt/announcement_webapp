import os

import boto3
from schemas import DbAnnouncementList


def handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table_name = os.environ.get('TABLE_NAME')
    table = dynamodb.Table(table_name)

    response = table.scan()
    announcements_data = response.get('Items', [])
    announcements = DbAnnouncementList(data=announcements_data, count=len(announcements_data))
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': announcements.json(),
    }
