"""
This file is for xyz reason
"""

# Library imports
from firebase_admin import messaging
from typing import Any


class APSAlert:
    """
    This class does xyz
    """

    def __init__(
        self,
        title: str,
        subtitle: str,
        body: str,
        loc_key: str,
        loc_args: str,
        title_loc_key: str,
        action_loc_key: str,
        launch_image: str,
        custom_data: dict,
    ):
        """
        :param: this param is for xyz
        """
        self.APSAlertInput = {
            "title": title,
            "subtitle": None,
            "body": body,
            "loc_key": None,
            "loc_args": None,
            "title_loc_key": None,
            "action_loc_key": None,
            "launch_image": None,
            "custom_data": custom_data,
        }

    def create_obj(self):
        return messaging.ApsAlert(**self.APSAlertInput)


class APSInput:
    """
    This class does xyz
    """

    def __init__(
        self,
        alert: Any,
        badge: int,
        sound: str,
        content_available: str,
        category: str,
        thread_id: str,
        mutable_content: str,
        custom_data: dict,
    ):
        """
        :param: this param is for xyz
        """
        self.APSInput = {
            "alert": alert,
            "badge": badge,
            "sound": sound,
            "content_available": None,
            "category": None,
            "thread_id": None,
            "mutable_content": None,
            "custom_data": custom_data,
        }

    def create_obj(self):
        return messaging.Aps(**self.APSInput)


class APS:
    """
    This class does xyz
    """

    def __init__(self, APSInput: Any):
        """
        :param: this param is for xyz
        """
        self.APSInput = APSInput

    def create_obj(self):
        return messaging.Aps(APSInput)


class APNSPayload:
    """
    This class does xyz
    """

    def __init__(self, APS: Any):
        """
        :param: this param is for xyz
        """
        self.APS = APS

    def create_obj(self):

        return messaging.APNSPayload(aps=self.APS)


class APNSConfig:
    """
    This class does xyz
    """

    def __init__(self, APNSPayload: Any, APNSFCMOptions: Any, APNSFCMHeaders: Any):
        """
        :param: this param is for xyz
        """
        self.APNSConfigInput = {
            "headers": APNSFCMHeaders,
            "payload": APNSPayload,
            "fcm_options": APNSFCMOptions,
        }

    def create_obj(self):
        return messaging.APNSConfig(**self.APNSConfigInput)
