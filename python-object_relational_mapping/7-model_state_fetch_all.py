#!/usr/bin/python3
"""List all State objects using sqlalchemy"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_states(username, passwd, database):
    """Lists all State objects

    Args:
        username (str): Username to connect to SQL server
        passwd (str): Password to SQL server
        database (str): Database name
    """

    # Create engine and connect to database
    engine = create_engine(
        f'mysql+mysldb://{username}:{passwd}@localhost:3306/{database}'
    )

    # Set up all data to use
    Base.metadata.create_all(bind=engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to select all states
    states = session.query(State).order_by(State.id).all()

    # Print states
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit()

    username = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]

    list_states(username, passwd, database)
