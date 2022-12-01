import time,datetime

from fastapi import FastAPI


from app.adapters.notifications.models.Notifications import ClassroomNotificationInputModel, MessageSuccessModel
from app.adapters.notifications.models.AppleModel import AppleInputModel

from app.adapters.notifications.fcm_adapters.AppleAdapter import AppleAdapter
from app.adapters.notifications.fcm_adapters.MessageAdapter import Message

from app.adapters.notifications.utils.firebase_helper import fcm_wrapper

import firebase_admin
from app.config import settings
from firebase_admin import credentials

# from motor.motor_asyncio import AsyncIOMotorClient

firebase = firebase_admin.initialize_app(
        credentials.Certificate(settings.GOOGLE_APP_CREDENTIALS)
    )
# mongodb = AsyncIOMotorClient(settings.MONGODB_URL)


def classroom_notification(
    notification: ClassroomNotificationInputModel
):
    """
    Send notification to all devices subscribed to a topic
    """
    print("=====================2222222222222222222222222=======================")

    # Convert the input to dictionary
    notification = notification.dict()

    # metrics
    sent: int = 0
    failed: int = 0

    topic = notification["topic"]
    payload = fcm_wrapper(notification["payload"])
    title = payload["title"]
    body = payload["body"]
    image = payload["image"]
    # added for TTL index
    notification["expireAt"] = datetime.datetime.utcnow()

    # TODO: Check if topic is a valid classroom

    """
    TODO: REMOVE dis shit cuz android don want it
    ## common notification object
    common_config = NotificationInputModel(title=title, body=body, image=image)
    commoncfg = CommonNotification(model=common_config).create()
    
    """

    androidcfg = None

    aps_kwargs = AppleInputModel(
        title=title,
        body=body,
        badge=11,
        sound="default",
        aps_custom_data=payload,
        aps_alert_custom_data=payload,
    )

    applecfg = AppleAdapter(aps_kwargs).create_obj()

    try:
        # FCM message constructor
        message = Message(
            data=payload,
            topic=topic,
            notification=None,
            android=androidcfg,
            apns=applecfg,
            app=firebase,       # request needed??
        )
    

        # Message trigger
        sent = message.send()
        print("===================3333333333333333333======================")


    except Exception as e:

        print({"Error in classroom_notification": e})

        return MessageSuccessModel(success=False, message_id=sent)

    # mongodb.user_data.classroom_notification.insert_one(notification)       # request needed??

    return MessageSuccessModel(success=True, message_id=sent)
