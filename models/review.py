#!/usr/bin/python3
""" Model for the review inheriting from the base model """

from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from models import storage_switch


class Review(BaseModel):
    """
    The Review model

    Arguments:
        __tablename__: Database table
        place_id (str): Unique Place id.
        user_id (str): Unique user id.
        text (str): Review.
    """
    if storage_switch == 'db':
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
