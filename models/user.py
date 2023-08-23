#!/usr/bin/python3
""" Model for the User inheriting from the base model """
import models
import sqlalchemy
from sqlalchemy import Column, String, Integer
from models.base_model import BaseModel


class User(BaseModel):
    """
    The User model

    Arguments:
        email (str): User email.
        password (str): User password.
        first_name (str): User first name.
        last_name (str): User last name.
        age (int): User age.

    """

    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    age = Column(Integer, nullable=True)

