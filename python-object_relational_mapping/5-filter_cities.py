#!/usr/bin/python3
"""
This script lists all cities of a given state from the database hbtn_0e_4_usa.
Usage: ./5-filter_cities.py <mysql username> <mysql password>
                                  <database name> <state name>
Results are sorted by cities.id in ascending order.
SQL injection safe.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py <username> <password> <database> <state>")
        sys.exit(1)

    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password,
                             db=database, charset="utf8")
        cursor = db.cursor()
        query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """
        cursor.execute(query, (state_name,))
        results = cursor.fetchall()
        print(", ".join([row[0] for row in results]))
    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()
