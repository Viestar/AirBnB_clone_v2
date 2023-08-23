#!/usr/bin/python3
""" File storage Class Model"""


import json
import os
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.review import Review
from models.state import State
from models.amenity import Amenity
from models.place import Place


class FileStorage():
    """ Serializes instances to a JSON file and vice versa """

    __file_path = "faith.json"
    __objects = {}

    def all(self, cls=None):
        """Returns the dictionary __objects of a given class"""
        if cls is None:
            return self.__objects
        else:
            cls_objects = {}
            for key, value in self.__objects.items():
                if isinstance(value, cls):
                    cls_objects[key] = value
            return cls_objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serializes a class dict into a JSON file for storage"""
        with open(self.__file_path, 'w', encoding='utf-8') as viestar:
            storage_dic = {}
            for key, value in self.__objects.items():
                storage_dic[key] = value.to_dict()
            json.dump(storage_dic, viestar)

    def reload(self):
        """ Deserializes a JSON file into a dictionary """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as faith:
                for object in json.load(faith).values():
                    self.new(eval(object["__class__"])(**object))
        else:
            # Incase file doesn't exist, return with nothing
            return

    def delete(self, obj=None):
        """ Deletes an object if its inside """
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
        else:
            return
