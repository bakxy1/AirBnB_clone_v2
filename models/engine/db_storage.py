#!/usr/bin/python3
"""Module defines class `DBStorage`"""


import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from models.base_model import Base, BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


types = {
    "State": State,
    "City": City,
    "User": User,
    "Place": Place,
    "Review": Review,
}


class DBStorage:
    """DBStorage class"""

    __engine = None
    __session = None

    def __init__(self):
        """Constructor"""
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}:3306/{}".format(
                os.getenv("HBNB_MYSQL_USER"),
                os.getenv("HBNB_MYSQL_PWD"),
                os.getenv("HBNB_MYSQL_HOST"),
                os.getenv("HBNB_MYSQL_DB"),
            ),
            pool_pre_ping=True,
        )

        if os.getenv("HBNB_ENV") == "test":
            self.__engine.metadata.drop_all()

    def all(self, cls=None):
        """Query current session for all objects associated with `cls`"""
        all_instances = {}

        if cls is not None:
            cls_instances = self.__session.query(cls).all()
            for instance in cls_instances:
                all_instances[cls.__name__ + "." + instance.id] = instance
        else:
            for k, v in types.items():
                cls_instances = self.__session.query(v).all()
                for instance in cls_instances:
                    all_instances[k + "." + instance.id] = instance

        return all_instances

    def new(self, obj):
        """Add the object to current session"""
        self.__session.add(obj)

    def save(self):
        """Save to session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete uncommited objects"""
        self.__session.delete(obj) if obj else None

    def reload(self):
        """create current database session"""
        Base.metadata.create_all(self.__engine)

        self.__session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )()
