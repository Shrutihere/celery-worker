from urllib import response
from pydantic import BaseModel, Field
from app.models.ObjectId import ObjectId
from typing import Any, List


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


class UserPayload(BaseModel):
    title: str
    body: str
    image: str = ""
    kind: int  # Species what the notification is for - feed, material assignment
    created_at: int
    created_by: str
    classroom_id: ObjectId = None
    item_id: List[str] = []
    action: bool = False
    action_path: List[str] = []
    extra_path: str = ""

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class FCMPayload(
    BaseModel
):  # NOTE: All keys and values in the dictionary must be strings
    # FCM Documentation: https://firebase.google.com/docs/reference/admin/python/firebase_admin.messaging#message
    title: str
    description: str
    kind: str
    classroom_id: str
    created_at: str
    created_by: str
    item_id: str
    action: str
    action_path: str
    extra_path: str


class RegistrationTokenInputModel(BaseModel):
    username: str
    tokens: List[str]
    updated_at: int


class RegistrationTokenOutputModel(BaseModel):
    id: ObjectId = Field(alias="_id")
    username: str
    tokens: List[str]
    updated_at: int

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class ClassroomTopicInputModel(BaseModel):
    classroom_id: ObjectId = Field(alias="_id")
    tokens: List[ObjectId]  # of RegistrationToken
    topic: str
    updated_at: int


class ClassroomTopicOutputModel(BaseModel):
    classroom_id: ObjectId = Field(alias="_id")
    tokens: List[ObjectId]  # of RegistrationToken
    topic: str
    updated_at: int

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class UserNotificationInputModel(BaseModel):
    username: str
    payload: UserPayload


class UsersNotificationInputModel(BaseModel):
    usernames: List[str]
    payload: UserPayload


class UserNotificationOutputModel(BaseModel):
    id: ObjectId = Field(alias="_id")
    username: str
    payload: Payload

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


class ClassroomNotificationOutputModel(BaseModel):
    id: ObjectId = Field(alias="_id")
    classroom_id: ObjectId = Field(alias="_id")
    topic: str
    payload: Any

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class TopicManagerInputModel(BaseModel):
    token: List[str]
    topic: str


class TopicManagerOutputModel(BaseModel):
    count: int


class TokenManagerInputModel(BaseModel):
    token: str


class TokenManagerOutputModel(BaseModel):
    pass


class SingleDeviceInputModel(BaseModel):
    token: str
    payload: Payload


class SingleDeviceOutputModel(BaseModel):
    pass


class SingleUserInputModel(BaseModel):
    payload: Payload


class SingleUserOutputModel(BaseModel):
    pass


class MultiDeviceInputModel(BaseModel):
    payload: Payload
    tokens: List[RegistrationTokenInputModel]


class MultiDeviceOutputModel(BaseModel):
    pass


class MultiUserInputModel(BaseModel):
    payload: Payload
    usernames: List[str]


class MultiUserOutputModel(BaseModel):
    pass


class BasicSucessModel(BaseModel):
    success: bool


class MessageSuccessModel(BaseModel):
    success: bool
    message_id: str
