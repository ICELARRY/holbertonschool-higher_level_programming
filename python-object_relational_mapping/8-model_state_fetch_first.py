#!/usr/bin/python3
"""
Script that prints the first State object from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    if len(sys.argv) != 4:
        print("Usage: ./8-model_state_fetch_first.py <user> <password> <database>")
        return

    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create the SQLAlchemy engine
    engine = create_engine(f"mysql+mysqldb://{user}:{password}@localhost:3306/{db_name}")

    # Bind Base metadata to the engine
    Base.metadata.bind = engine

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Get the first state ordered by id
        first_state = session.query(State).order_by(State.id).first()

        if first_state is None:
            print("Nothing")
        else:
            print(f"{first_state.id}: {first_state.name}")

    except Exception as e:
        print("Error:", e)
    finally:
        session.close()

if __name__ == "__main__":
    main()
