#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Meta = MetaData()
Base = declarative_base(metadata=Meta)

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=True)
    cities = relationship("City", backref="states")
