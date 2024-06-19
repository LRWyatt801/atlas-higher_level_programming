#!/usr/bin/python3
"""Module lists all states in database"""


import MySQLdb
import sys


def list_states(username, passwd, database):
    """ Lists all the states """

    # connect to database
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=passwd,
        db=database
    )

    # Create cursor
    cur = db.cursor()

    # Execute query
    cur.execute("SELECT * FROM states ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]

    list_states(username, passwd, database)
