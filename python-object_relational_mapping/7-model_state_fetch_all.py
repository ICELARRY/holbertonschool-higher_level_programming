#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.
Usage: ./7-model_state_fetch_all.py <username> <password> <database>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./7-model_state_fetch_all.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
    )

    # Bind session to engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states sorted by id
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()
