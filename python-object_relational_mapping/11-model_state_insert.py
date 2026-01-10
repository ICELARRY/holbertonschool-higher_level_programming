#!/usr/bin/python3
"""
Add the State "Louisiana" to the database hbtn_0e_6_usa
Usage: ./11-model_state_insert.py <mysql username> <mysql password> <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Add a new State 'Louisiana' and print its id"""
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        return

    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create the engine and connect
    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add the new State
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print the id of the new state
    print(new_state.id)

    # Close the session
    session.close()


if __name__ == "__main__":
    main()
