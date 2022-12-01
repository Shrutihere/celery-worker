from bson import ObjectId as BsonObjectId
# from bson.errors import InvalidId
from pydantic import BaseConfig, BaseModel
from pydantic import Field as PydanticField


class ObjectId(BsonObjectId):
    """
    This class defines the type for a mongoDB ObjectId
    """

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        # try:
            # try to validate id, if fails Error raise
            return ObjectId(str(v))
        # If error raises, send not a valid objectId error message
        # except InvalidId:
        #     raise ValueError("Not a valid ObjectId")
