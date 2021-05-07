from aws_cdk import aws_apigateway, aws_dynamodb, aws_lambda, aws_lambda_python
from aws_cdk import core as cdk


class AnnouncementWebappStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        announcements_table = aws_dynamodb.Table(
            scope=self,
            id='announcements_table',
            partition_key=aws_dynamodb.Attribute(
                name='id',
                type=aws_dynamodb.AttributeType.STRING,
            ),
        )
        api = aws_apigateway.RestApi(
            scope=self,
            id='announcements_rest_api_gateway',
        )
        announcements_endpoint = api.root.add_resource('announcements')

        get_announcements_handler = aws_lambda_python.PythonFunction(
            scope=self,
            id='GetAnnouncementHandler',
            entry='lambda',
            index='get.py',
            handler='handler',
            runtime=aws_lambda.Runtime.PYTHON_3_8,
        )
        create_announcement_handler = aws_lambda_python.PythonFunction(
            scope=self,
            id='CreateAnnouncementHandler',
            entry='lambda',
            index='create.py',
            handler='handler',
            runtime=aws_lambda.Runtime.PYTHON_3_6,
        )
        announcements_table.grant_read_data(get_announcements_handler)
        announcements_table.grant_read_write_data(create_announcement_handler)
        get_announcements_handler.add_environment('TABLE_NAME', announcements_table.table_name)
        create_announcement_handler.add_environment('TABLE_NAME', announcements_table.table_name)
        get_announcements_integration = aws_apigateway.LambdaIntegration(get_announcements_handler)
        create_announcements_integration = aws_apigateway.LambdaIntegration(create_announcement_handler)
        announcements_endpoint.add_method('GET', get_announcements_integration)
        announcements_endpoint.add_method('POST', create_announcements_integration)
