#!/usr/bin/python3
"""
Prints the id of the State object with a given name from the database.
Usage: ./10-model_state_my_get.py <username> <password> <database> <state_name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Connects to the database and prints the id of a specific state."""
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        return

    username, password, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Create engine and session
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query state safely (SQL injection-free)
    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    main()
