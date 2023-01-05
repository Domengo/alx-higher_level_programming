#!/usr/bin/python3

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import (create_engine)


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                            .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    i = session.query(State).filter(State.name.like ('%a%')).all()
    for states in i:
        print(f"{states.id}: {states.name}")
    session.close()
