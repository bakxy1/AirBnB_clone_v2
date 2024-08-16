#!/usr/bin/python3
"""Defines the base model of a type"""

from uuid import uuid4
from copy import deepcopy
from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()


class BaseModel:
    """Parent class"""

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())

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
        from models import storage

        self.updated_at = datetime.now()

        storage.new(self)
        storage.save()

    def to_dict(self):
        """Return dictionary of instance"""
        instance_dict = {}
        instance_dict.update(self.__dict__)

        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()

        instance_dict.pop("_sa_instance_state", None)

        return instance_dict

    def delete(self):
        """Delete current instance from storage"""
        from models import storage

        storage.delete(self)
