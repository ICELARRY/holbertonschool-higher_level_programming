#!/usr/bin/python3
"""Lists all states with names starting with N from a database."""

import sys
import MySQLdb


def main():
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    cur = db.cursor()
    cur.execute(
        "SELECT id, name FROM states "
        "WHERE name LIKE 'N%' "
        "ORDER BY id ASC"
    )

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
