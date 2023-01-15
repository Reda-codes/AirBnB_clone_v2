#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    class State(BaseModel, Base):
        """ State class """

        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade="all, delete", backref='state')
else:
    class State(BaseModel):
        """ State class """

        name = Column(String(128), nullable=False)

        @property
        def cities(self):
            """City objects getter"""
            from models import storage
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
