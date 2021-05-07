from datetime import date
from typing import List, Union

from pydantic.class_validators import validator
from pydantic.main import BaseModel


class BaseAnnouncement(BaseModel):
    title: str
    description: str
    date: date


class CreateAnnouncement(BaseAnnouncement):
    date: Union[date, str]

    @validator('date')
    def cast_date(cls, v):
        if isinstance(v, str):
            return v
        return str(v)


class DbAnnouncement(BaseAnnouncement):
    id: str


class DbAnnouncementList(BaseModel):
    count: int
    data: List[DbAnnouncement]
