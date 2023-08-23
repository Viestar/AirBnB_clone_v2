#!/usr/bin/python3
""" Model for the city inheriting from the base model """

from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models import storage_switch


class City(BaseModel, Base):
    """
    The City model

    Arguments:
        __table__(str): Database table name
        state_id (str): Unique State id.
        name (str): State name.
    """
    __tablename__ = "cities"
    if storage_switch == 'db':
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship('Place', backref='cities',
                              cascade='all, delete, delete-orphan')
    else:
        state_id = ""
        name = ""
