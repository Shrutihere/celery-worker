"""
This file has xyz things
"""

#
# Local imports
#
from typing import List, Union
from app.adapters.notifications.models.Notifications import (
    Payload,
    ClassroomNotificationInputModel,
    UserNotificationInputModel,
    UsersNotificationInputModel,
    UserPayload,
)

from app.constants import (
    TIMELINE_NOTIFICATION_ENDPOINT_DEBUG,
    TIMELINE_NOTIFICATION_ENDPOINT_PROD,
    USERS_NOTIFICATION_ENDPOINT_DEBUG,
    USERS_NOTIFICATION_ENDPOINT_PROD
)
from app.adapters.notifications.methods.edvora_request import EdvoraRequest

#
# Library imports
#
# from rich import print


class EdvoraNotification:
    """
    This class is for xyz things
    """

    notification = None
    auth_header = None
    endpoint_url = None
    kind = None
    classroom_id = None
    topic = None

    def __init__(
        self,
        auth_header,
        title: str,
        body: str,
        created_at: int,
        created_by: str,
        classroom_id: str,
        kind: int,
        item_id: List[str] = [],
        action_path: List[str] = [],
        action: bool = False,
        image: str = "",
        extra_path: str = "",
        debug: bool = False,
    ):
        """
        This method does xyz
        :param:
        """

        self.auth_header = auth_header

        self.endpoint_url = (
            TIMELINE_NOTIFICATION_ENDPOINT_DEBUG
            if debug
            else TIMELINE_NOTIFICATION_ENDPOINT_PROD
        )

        self.kind = kind

        self.classroom_id = classroom_id

        self.topic = str(classroom_id)

        self.notification = ClassroomNotificationInputModel(
            classroom_id=str(classroom_id),
            topic=self.topic,
            payload=Payload(
                title=title,
                body=body,
                kind=kind,
                image=image,
                classroom_id=str(classroom_id),
                created_at=created_at,
                created_by=created_by,
                item_id=item_id,
                action=action,
                action_path=action_path,
                extra_path=extra_path,
            ),
        )

    def send(self):
        """
        This functin does xyz
        """

        client = EdvoraRequest(
            auth_headers=self.auth_header,
            endpoint=self.endpoint_url,
        )
        # print(self.notification.dict())
        print("==========================================000000000000000000000000000000000=======================")

        try:

            client.post_request(
                body=self.notification,
            )

        except Exception as exception:

            print(
                {
                    "Notification Error": exception,
                    "Class": self.classroom_id,
                    "Location": "EdvoraNotification",
                }
            )

            raise Exception(exception)


class EdvoraUserNotification:
    """
    This class is for xyz things
    """

    notification = None
    auth_header = None
    endpoint_url = None
    kind = None
    classroom_id = None
    topic = None

    def __init__(
        self,
        auth_header,
        username: Union[str, List[str]],
        title: str,
        body: str,
        created_at: int,
        created_by: str,
        kind: int,
        item_id: List[str] = [],
        action_path: List[str] = [],
        action: bool = False,
        image: str = "",
        extra_path: str = "",
        debug: bool = False,
    ):
        """
        This method does xyz
        :param:
        """

        self.auth_header = auth_header

        # TODO: verify username
        self.username = username

        self.kind = kind

        if isinstance(self.username, str):

            self.endpoint_url = (
                USERS_NOTIFICATION_ENDPOINT_DEBUG
                if debug
                else USERS_NOTIFICATION_ENDPOINT_PROD
            )

            self.notification = UserNotificationInputModel(
                username=self.username,
                payload=UserPayload(
                    title=title,
                    body=body,
                    kind=kind,
                    image=image,
                    created_at=created_at,
                    created_by=created_by,
                    item_id=item_id,
                    action=action,
                    action_path=action_path,
                    extra_path=extra_path,
                ),
            )

        elif isinstance(self.username, list):

            self.endpoint_url = (
                USERS_NOTIFICATION_ENDPOINT_DEBUG
                if debug
                else USERS_NOTIFICATION_ENDPOINT_PROD
            )

            self.notification = UsersNotificationInputModel(
                usernames=self.username,
                payload=UserPayload(
                    title=title,
                    body=body,
                    kind=kind,
                    image=image,
                    created_at=created_at,
                    created_by=created_by,
                    item_id=item_id,
                    action=action,
                    action_path=action_path,
                    extra_path=extra_path,
                ),
            )

    def send(self):
        """
        This functin does xyz
        """

        client = EdvoraRequest(
            auth_headers=self.auth_header,
            endpoint=self.endpoint_url,
        )

        try:

            client.post_request(
                body=self.notification.dict(),
            )

        except Exception as exception:

            print(
                {
                    "Single User Notification Error": exception,
                    "User": self.username,
                    "Location": "EdvoraUserNotification",
                }
            )

            raise Exception(exception)
