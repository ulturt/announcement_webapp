from datetime import datetime
from typing import List

from pydantic.main import BaseModel


class BaseAnnouncement(BaseModel):
    title: str
    description: str


class CreateAnnouncement(BaseAnnouncement):
    pass


class DbAnnouncement(BaseAnnouncement):
    id: str
    date: datetime


class DbAnnouncementList(BaseModel):
    count: int
    data: List[DbAnnouncement]
