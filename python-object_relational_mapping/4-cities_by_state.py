#!/usr/bin/python3
""" Takes an argument and displays all the values """

import MySQLdb
import sys


def list_cities(username, passwd, database):
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
    cur.execute("SELECT cities.id, cities.name, states.name FROM states "
        + "INNER JOIN cities ON cities.state_id = states.id "
        + "ORDER BY cities.id")

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

    list_cities(username, passwd, database)
