#!/usr/bin/python3
"""Module defines storage class"""


import json


class FileStorage:
    """File storage class"""

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Constructor"""
        pass

    def all(self, cls=None):
        """Returns __objects"""
        cls_objects = {}
        if not cls:
            return self.__class__.__objects

        for id, state in self.__class__.__objects.items():
            if type(state) is cls:
                cls_objects[id] = state

        return cls_objects

    def new(self, obj):
        """Sets new object to __objects"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes to a file"""
        dct = {}
        for k, v in self.__objects.items():
            dct[k] = v.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(dct, file)

    def reload(self):
        """Loads objects from file"""

        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State

        cls = {
            "BaseModel": BaseModel,
            "User": User,
            "Amenity": Amenity,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
        }

        dct = None
        try:
            with open(self.__file_path, "r") as file:
                dct = json.load(file)
            for k, v in dct.items():
                self.__objects[k] = cls.get(k.split(".")[0])(**v)
        except Exception:
            pass

    def delete(self, obj=None):
        """Delete object from __objects dictinoary"""
        if obj:
            for k, v in self.__class__.__objects.items():
                if obj is v:
                    del self.__class__.__objects[k]
                    break
