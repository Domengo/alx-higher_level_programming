#!/usr/bin/python3
"""
lists all states from db hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]))
    session = Session(bind=engine)
    states = session.query(State).order_by(State.id).filter(State.id == 1).all()

    for row in states:
        if (row == 0):
            print("Nothing", end="")
        else:
            print(f"{row.id}: {row.name}")
