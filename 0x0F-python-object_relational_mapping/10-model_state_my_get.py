#!/usr/bin/python3

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import (create_engine)


if __name__ == '__main__':
    state_name = argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                            .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    i = session.query(State).filter(State.name == state_name).first()
    if i:
        print(i.id)
    else:
        print("Not found")

    session.close()
