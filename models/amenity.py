#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    class Amenity(BaseModel, Base):
        """ Defines the Amenity class """

        __tablename__ = 'amenities'
        __table_args__ = ({'mysql_default_charset': 'latin1'})
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
                'Place', secondary=Place.place_amenity,
                back_populates='amenities')
else:
    class Amenity(BaseModel):
        """ Defines the Amenity class """
        name = ""
