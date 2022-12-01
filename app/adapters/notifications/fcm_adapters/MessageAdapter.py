"""
This file is for xyz reason
"""

# Library imports
from typing import Any, Optional, List
from firebase_admin import messaging

# Local imports
from app.adapters.notifications.models.Notifications import FCMPayload


class Message:
    """
    This class does xyz
    """

    token = None
    tokens = None
    topic = None
    messaging = None

    def __init__(
        self,
        data: FCMPayload,
        notification: Any,
        android: Any,
        apns: Any,
        app: Any,
        token: Optional[str] = None,
        tokens: Optional[List[str]] = None,
        topic: Optional[str] = None,
    ):
        """
        :param: this param is for that
        """
        if topic:
            self.topic = "/topics/" + topic
            self.messaging = messaging.Message(
                data=data,
                topic=topic,
                notification=notification,
                android=android,
                apns=apns,
            )

        elif token:
            self.token = token
            self.messaging = messaging.Message(
                data=data,
                token=token,
                notification=notification,
                android=android,
                apns=apns,
            )

        elif tokens != []:
            self.tokens = tokens
            self.messaging = messaging.MulticastMessage(
                tokens=tokens,
                data=data,
                notification=notification,
                android=android,
                apns=apns,
            )

        else:
            raise Exception(
                {
                    "MessageAdapter": "Atleast one of topic, token, tokens should be given"
                }
            )

        self.app = app

    def send(self):
        """
        This function does that
        """

        if self.tokens:
            return messaging.send_multicast(self.messaging, app=self.app)

        else:
            print("===================4444444444444444444444444======================")
            a = messaging.send(self.messaging, app=self.app)
            print(a)
            return a
