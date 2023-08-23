#!/usr/bin/python3
""" Model for the state inheriting from the base model """

from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import models
from os import getenv
from models.city import City


class State(BaseModel):
    """
    The State model

    Argument:
        __table__: Database table name
        name (str): State name.
    """

    if getenv("HBNB_TYPE_STORAGE") == "db":
        __table__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")
    else:
        @property
        def cities(self):
            """Fetchees related City objects from file storage."""
            cities_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
