#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    class City(BaseModel, Base):
        """ The city class, contains state ID and name """
        __tablename__ = "cities"
        __table_args__ = ({'mysql_default_charset': 'latin1'})
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', cascade='delete', backref='cities')

else:
    class City(BaseModel):
        """ The city class, contains state ID and name """
        state_id = ""
        name = ""
