#!/usr/bin/python3
""" Takes an argument and displays all the values """

import MySQLdb
import sys


def state_filter(username, passwd, database, state):
    """Filters database and displays state

    Args:
        username (str): Username of user
        passwd (str): password for user
        database (str): name of database
        state (str): State to search for
    """
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
    query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cur.execute(query, (state,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    username = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    state_filter(username, passwd, database, state)
