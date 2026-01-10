#!/usr/bin/python3
"""
This script lists all states with a name starting with N (uppercase)
from the database hbtn_0e_0_usa.
Usage: ./1-filter_states.py <username> <password> <database_name>
"""

import MySQLdb
import sys


def main():
    """ Main function to fetch states starting with N """
    if len(sys.argv) != 4:
        return

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=password, db=db_name)

    cursor = db.cursor()

    # Execute SQL query with case-sensitive filter
    query = "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Fetch and print all results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
