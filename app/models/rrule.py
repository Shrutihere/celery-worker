import time
from typing import List, Union

from pydantic import BaseModel, validator
from fastapi import FastAPI, BackgroundTasks

from app.adapters.notifications.methods.edvora_notification import EdvoraNotification




class RRule(BaseModel):

    """
    This class represents the recurrence definition
    """

    dtstart: int = None
    freq: int
    interval: int = 1
    wkst: int = None
    until: int = None
    bysetpos: List[int] = None
    bymonth: List[int] = None
    bymonthday: List[int] = None
    byyearday: List[int] = None
    byweekno: List[int] = None
    byweekday: List[int] = None
    byhour: List[int] = None
    byminute: List[int] = None
    bysecond: List[int] = None
    cache: int = None

    @validator("freq")
    def checkFreq(cls, value):
        if value > 3:
            raise ValueError("freq can't be bigger than 3")
        return value

    @validator("bysetpos")
    def checkBySetPOS(cls, value):
        if value is not None:
            if (0 in value) or (max(value) > 366) or (min(value) < -366):
                raise ValueError(
                    "bysetpos must be between 1 and 366, or between -366 and -1"
                )
        return value


class Task(BaseModel):
    rrule: RRule = None
    start_datetime: int
    notification_metadata: dict
