#!/usr/bin/python3
"""
create state class that inherits from base
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData

mymetadata = MetaData()
Base = declarative_base()


class State(Base):
    """
    class with id and name attributes of each state
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
