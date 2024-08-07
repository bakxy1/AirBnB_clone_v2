#!/usr/bin/python3
"""Defines the base model of a type"""

from uuid import uuid4
from copy import deepcopy
from datetime import datetime


class BaseModel:
    """Parent class"""

    def __init__(self, *_, **kwargs):
        """Constructor method"""
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "created_at" or k == "updated_at":
                        setattr(self, k, datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = deepcopy(self.created_at)

    def __str__(self) -> str:
        """Overrides string method"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates update time attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dictionary of instance"""
        instance_dict = {}
        instance_dict.update(self.__dict__)

        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()

        return instance_dict
