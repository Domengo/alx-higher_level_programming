#!/usr/bin/python3
"""
lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]))
    session = Session(bind=engine)
    states = session.query(State).order_by\
            (State.id).filter(State.name.like('%a%')).all()

    for row in states:
        print(f"{row.id}: {row.name}")
