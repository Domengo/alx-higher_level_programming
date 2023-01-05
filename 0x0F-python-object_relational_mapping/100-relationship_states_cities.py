#!/usr/bin/python3

from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import (create_engine)
from relationship_city import City


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                            .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    new_state = State(name='California')
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)

    session.add(new_city)
    session.add(new_state)
    session.commit()

    session.close()
