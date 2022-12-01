from pydantic import BaseModel


class AndroidInputModel(BaseModel):
    title: str
    body: str
    icon: str
    color: str
    sound: str
    tag: str
    click_action: str
    body_loc_key: str
    body_loc_args: str
    title_loc_key: str
    title_loc_args: str
    channel_id: str
    image: str
    ticker: str
    sticky: str
    notification_priority: str
    vibrate_timings_millis: str
    default_vibrate_timings: str
    default_sound: str
    light_settings: str
    default_light_settings: str
    visibility: str
    notification_count: str
    collapse_key: str
    config_priority: str
    ttl: str
    restricted_package_name: str
    data: str
    fcm_options: str
