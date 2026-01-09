#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""

import pymysql
import sys

if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    conn = pymysql.connect(host="localhost",
                           user=username,
                           password=password,
                           database=db_name)
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)
    
    cur.close()
    conn.close()

