#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
where the state name matches the argument passed.
Usage: ./2-my_filter_states.py <username> <password> <database> <state_name>
"""

import MySQLdb
import sys


def main():
    """Main function to connect to the database and filter states."""
    if len(sys.argv) != 5:
        return

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=password, db=db_name)
    cursor = db.cursor()

    # Prepare SQL query
    sql = ("SELECT * FROM states "
           "WHERE name = '{}' "
           "ORDER BY id ASC").format(state_name)

    cursor.execute(sql)

    # Fetch and display results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
