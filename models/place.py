#!/usr/bin/python3
""" Model for the place inheriting from the base model """

from models.base_model import BaseModel
from models import storage_switch
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy import Float
from sqlalchemy.orm import relationship


class Place(BaseModel):
    """
    The Place model

    Arguments:
        city_id (str): Unique City id.
        user_id (str): Unique user id.
        name (str): Place name.
        description (str): Place Description.
        number_rooms (int): Number of the rooms.
        number_bathrooms (int): Number of bathrooms.
        max_guest (int): Maximum number of guests.
        price_by_night (int): Price by night.
        latitude (float): Place latitude.
        longitude (float): Place longitude.
        amenity_ids (list): A list of Amenity ids.
    """
    if storage_switch == 'db':
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, default=0, nullable=True)
        longitude = Column(Float, default=0, nullable=True)
        amenity_ids = []
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
