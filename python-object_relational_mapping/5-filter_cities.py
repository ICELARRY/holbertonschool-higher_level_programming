#!/usr/bin/python3
"""
Lists all cities of a given state from the database `hbtn_0e_4_usa`.
Usage: ./5-filter_cities.py <username> <password> <database> <state_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py <username> <password> "
              "<database> <state_name>")
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:]

    try:
        db = MySQLdb.connect(host="localhost",
                             user=username,
                             passwd=password,
                             db=database,
                             charset="utf8")
        cursor = db.cursor()

        query = (
            "SELECT cities.name "
            "FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "WHERE states.name = %s "
            "ORDER BY cities.id"
        )
        cursor.execute(query, (state_name,))
        cities = [row[0] for row in cursor.fetchall()]

        print(", ".join(cities))

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)
