#!/usr/bin/env python3
from aws_cdk import core

from announcement_webapp.announcement_webapp_stack import \
    AnnouncementWebappStack

app = core.App()
AnnouncementWebappStack(
    scope=app,
    construct_id='AnnouncementWebappStack',
)
app.synth()
