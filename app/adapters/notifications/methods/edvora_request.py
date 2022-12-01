"""
This file is for xyz
"""

#
# Library imports
#
import requests
from pydantic import BaseModel
from typing import List
from app.models.ObjectId import ObjectId
# from rich import print
from app.constants import TIMELINE_NOTIFICATION_ENDPOINT_PROD
from app.adapters.notifications.routers.notifications import classroom_notification
#
# Local imports
#
class Payload(BaseModel):
    title: str
    body: str
    image: str = ""
    kind: int  # Species what the notification is for - feed, material assignment
    classroom_id: str
    created_at: int
    created_by: str
    item_id: List[str] = ""
    action: bool = False
    action_path: List[str] = []
    extra_path: str = ""

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class ClassroomNotificationInputModel(BaseModel):
    classroom_id: str
    topic: str
    payload: Payload
    usernames: List[str] = []  # people who read this notification

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class EdvoraRequest:
    """
    This class is for xyz reason
    """

    auth_headers: str = ""
    endpoint: str = ""

    def __init__(self, auth_headers: str, endpoint: str):
        self.auth_headers = auth_headers
        self.endpoint = endpoint

    def post_request(self, body: dict):
        """
        This function does xyz
        """

        body = body
        try:
            print("=========================1111111111111111111111=======================")

            # req = requests.post(
            #     url=self.endpoint,
            #     headers={
            #         "Authorization": self.auth_headers,
            #     },
            #     json=body,
            # )
            classroom_notification(body)

            # req.raise_for_status()


        except requests.exceptions.HTTPError as err:
            print({"Notification Error": err, "Method": "post_request"})
            raise requests.exceptions.HTTPError

        except requests.exceptions.Timeout as err:
            print({"Notification Error": err, "Method": "post_request"})
            raise requests.exceptions.Timeout

        except requests.exceptions.TooManyRedirects as err:
            print({"Notification Error": err, "Method": "post_request"})
            raise requests.exceptions.TooManyRedirects

        except requests.exceptions.RequestException as err:
            print({"Notification Error": err, "Method": "post_request"})
            raise requests.exceptions.RequestException
