#!/usr/bin/python3

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_city import City


if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state, city in session.query(State, City).join(City).\
            order_by(City.id).all():
                print(f'{state.name}: ({city.id}) {city.name}')
    session.close()
