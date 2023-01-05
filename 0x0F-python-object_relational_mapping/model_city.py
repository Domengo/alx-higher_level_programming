#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, Sequence('city_id_seq'), primary_key=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

