from pydantic import BaseModel


class AppleInputModel(BaseModel):
    title: str = ""
    subtitle: str = ""
    body: str = ""
    loc_key: str = ""
    loc_args: str = ""
    title_loc_key: str = ""
    action_loc_key: str = ""
    launch_image: str = ""
    aps_alert_custom_data: dict
    badge: int = 11
    sound: str = ""
    content_available: str = ""
    category: str = ""
    thread_id: str = ""
    mutable_content: str = ""
    aps_custom_data: dict
