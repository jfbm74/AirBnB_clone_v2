#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, Integer, String
from models.city import City
from os import getenv
import models
from sqlalchemy.orm import relationship, backref


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        cascade="all,delete,delete-orphan",
        backref=backref("state", cascade="all,delete"),
        passive_deletes=True,
        single_parent=True)

    if getenv('HBNB_TYPE_STORAGE') == "db":
        cities = relationship(
            'City',
            cascade='all, delete-orphan',
            backref='state',
        )
    else:

        @property
        def cities(self):
            allcities = []
            for id, city in models.storage.all(City).items():
                if self.id == city.state_id:
                    allcities.append(city)
            return allcities
