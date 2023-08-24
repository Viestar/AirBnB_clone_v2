#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()


class BaseModel():
    """BaseModel defines all common attributes/methods for other classes
    Attributes:
        id (sqlalchemy String): The BaseModel id.
        created_at (sqlalchemy DateTime): time instance is born.
        updated_at (sqlalchemy DateTime): time instance is altered.
    """
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialising Common attributes of all subclasses"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # self.age = None  # Add the age attribute
            # self.password = None  # Add the password attribute
            # self.email = None  # Add the email attribute

    def save(self):
        """Updates the public updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance"""
        dict = self.__dict__.copy()
        dict['__class__'] = self.__class__.__name__
        for key in dict:
            if type(dict[key]) is datetime:
                dict[key] = dict[key].isoformat()
        if '_sa_instance_state' in dict.keys():
            del (dict['_sa_instance_state'])
        return dict

    def delete(self):
        """ Deletes current instance from the storage"""
        models.storage.delete()

    def __str__(self) -> str:
        """Returns: [class name] (ID) <class dictionary>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
