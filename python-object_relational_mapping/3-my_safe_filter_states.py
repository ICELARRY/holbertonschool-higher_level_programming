#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
where the state name matches the argument safely.
"""

import sys
import MySQLdb


def main():
    if len(sys.argv) != 5:
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    query = """
        SELECT id, name
        FROM states
        WHERE name = %s
        ORDER BY id ASC
    """
    cursor.execute(query, (state_name,))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
