#!/usr/bin/python3
""" Model for the User inheriting from the base model """

from models.base_model import BaseModel, Base
from sqlalchemy import Column
from sqlalchemy import String
from models import storage_switch


class User(BaseModel, Base):
    """
    The User model

    Arguments:
        __table: Database table
        email (str): User email.
        password (str): User password.
        first_name (str): User first name.
        last_name (str): User last name.
        age (int): User age.

    """
    __tablename__ = "users"
    if storage_switch == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        # places = relationship('Place', backref='user',
        #                       cascade='all, delete, delete-orphan')
        # reviews = relationship('Review', backref='user',
        #                        cascade='all, delete, delete-orphan')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
