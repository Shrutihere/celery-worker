"""
This file is for xyz reason"""

# Library imports
from pydantic import BaseModel


class NotificationInputModel(BaseModel):
    """This class does xyz"""

    title: str
    body: str
    image: str
