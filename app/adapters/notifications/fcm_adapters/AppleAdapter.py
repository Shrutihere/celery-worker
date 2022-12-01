"""
This file is for xyz reason
"""

# Library imports
from typing import Any
from firebase_admin import messaging

# Local imports
from app.adapters.notifications.fcm_adapters.APNSAdapter import (
    APSAlert,
    APSInput,
    APS,
    APNSConfig,
    APNSPayload,
)
from app.adapters.notifications.models.AppleModel import AppleInputModel


class AppleAdapter:
    """
    This class does xyz
    """

    def __init__(self, model: AppleInputModel):
        """
        :param: this param is for xyz
        """
        model = model.dict()
        # Comment
        Alert = APSAlert(
            title=model["title"],
            subtitle=model["subtitle"],
            body=model["body"],
            loc_key=model["loc_key"],
            loc_args=model["loc_args"],
            title_loc_key=model["title_loc_key"],
            action_loc_key=model["action_loc_key"],
            launch_image=model["launch_image"],
            custom_data=model["aps_alert_custom_data"],
        ).create_obj()

        # Comment
        Aps_input = APSInput(
            alert=Alert,
            badge=model["badge"],
            sound=model["sound"],
            content_available=model["content_available"],
            category=model["category"],
            thread_id=model["thread_id"],
            mutable_content=model["mutable_content"],
            custom_data=model["aps_custom_data"],
        ).create_obj()

        # Comment
        Aps = Aps_input
        # Comment
        self.Apns_payload = APNSPayload(APS=Aps).create_obj()

    def create_obj(self):

        # Comment
        return APNSConfig(
            APNSPayload=self.Apns_payload, APNSFCMHeaders=None, APNSFCMOptions=None
        ).create_obj()
