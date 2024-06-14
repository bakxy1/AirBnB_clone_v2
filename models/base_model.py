"""Defines the base model of a type"""

from uuid import uuid4
from datetime import datetime
from copy import deepcopy


class BaseModel:
    """Parent class"""

    def __init__(self) -> None:
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self) -> None:
        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        instance_dict = deepcopy(self.__dict__)
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        instance_dict["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return instance_dict
