#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
where the state name matches the argument passed (case-sensitive).
Usage: ./2-my_filter_states.py <username> <password> <database> <state_name>
"""

import MySQLdb
import sys


def main():
    """Connect to MySQL and display states matching the argument."""
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

    # SQL query with case-sensitive comparison
    sql = ("SELECT * FROM states "
           "WHERE BINARY name = '{}' "
           "ORDER BY id ASC").format(state_name)

    cursor.execute(sql)

    # Display results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
