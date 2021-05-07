import json
import os
import uuid

import boto3
from pydantic.error_wrappers import ValidationError
from schemas import CreateAnnouncement, DbAnnouncement


def handler(event, context):
    body = json.loads(event.get('body', ''))
    try:
        request_data = CreateAnnouncement(**body)
    except ValidationError as err:
        return {
            'statusCode': 400,
            'headers': {'Content-Type': 'application/json'},
            'body': err.json(),
        }

    dynamodb = boto3.resource('dynamodb')
    table_name = os.environ.get('TABLE_NAME')
    table = dynamodb.Table(table_name)

    new_announcement = request_data.dict()
    new_announcement['id'] = str(uuid.uuid4())
    table.put_item(Item=new_announcement)
    response = table.get_item(Key={'id': new_announcement['id']})
    announcement = DbAnnouncement(**response['Item'])
    return {
        'statusCode': 201,
        'headers': {'Content-Type': 'application/json'},
        'body': announcement.json(),
    }
