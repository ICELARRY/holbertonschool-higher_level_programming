#!/usr/bin/python3
"""
Adds the State "Louisiana" to the database hbtn_0e_6_usa
Usage: ./11-model_state_insert.py <username> <password> <database>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create engine
    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create new State
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print the new state's id
    print(new_state.id)

    # Close session
    session.close()
