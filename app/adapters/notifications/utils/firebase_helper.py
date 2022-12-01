"""
This file is for xyz reason
"""

# Local imports
from app.adapters.notifications.models.Notifications import FCMPayload, Payload


def fcm_wrapper(payload_object: Payload) -> FCMPayload:
    """
    This function is for xyz reason
    :param: this param does that
    """

    response = {
        "title": payload_object["title"],
        "body": payload_object["body"],
        "image": payload_object["image"],
        "kind": str(payload_object["kind"]),
        "classroom_id": str(payload_object["classroom_id"])
        if payload_object["classroom_id"]
        else "",
        "created_at": str(payload_object["created_at"]),
        "created_by": payload_object["created_by"],
        "item_id": ",".join(payload_object["item_id"]),
        "action": str(payload_object["action"]),
        "action_path": ",".join(payload_object["action_path"]),
        "extra_path": payload_object["extra_path"],
    }

    return response
