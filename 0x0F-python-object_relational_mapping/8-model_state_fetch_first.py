#!/usr/bin/python3
"""
lists the first state from db hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]))
    session = Session(bind=engine)
    states = session.query(State).first()

    if states is None:
        print("Nothing")
    else:
        print(f"{states.id}: {states.name}")
