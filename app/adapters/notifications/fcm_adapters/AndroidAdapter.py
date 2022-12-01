"""
This file is for xyz reason
"""

# Local imports
from src.interfaces.notification.models.AndroidModel import AndroidInputModel

# Library imports
from typing import Any
from firebase_admin import messaging


class AndroidAdapter:
    """
    This class does xyz
    """

    def __init__(self, model: AndroidInputModel):
        """
        :param: this param is for xyz
        """
        AndroidNotificationObject = messaging.AndroidNotification(
            title=model["title"],
            body=model["body"],
            icon=model["icon"],
            color=model["color"],
            sound=model["sound"],
            tag=model["tag"],
            click_action=model["click_action"],
            body_loc_key=model["body_loc_key"],
            body_loc_args=model["body_loc_args"],
            title_loc_key=model["title_loc_key"],
            title_loc_args=model["title_loc_args"],
            channel_id=model["channel_id"],
            image=model["image"],
            ticker=model["ticker"],
            sticky=model["sticky"],
            notification_priority=model["notification_priority"],
            vibrate_timings_millis=model["vibrate_timings_millis"],
            default_vibrate_timings=model["default_vibrate_timings"],
            default_sound=model["default_sound"],
            light_settings=model["light_settings"],
            default_light_settings=model["default_light_settings"],
            visibility=model["visibility"],
            notification_count=model["notification_count"],
        )

        AndroidConfig = messaging.AndroidConfig(
            collapse_key=model["collapse_key"],
            config_priority=model["config_priority"],
            ttl=model["ttl"],
            restricted_package_name=model["restricted_package_name"],
            data=model["data"],
            fcm_options=model["fcm_options"],
            notification=AndroidNotificationObject,
        )

        return AndroidConfig
