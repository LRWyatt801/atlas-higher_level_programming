#!/usr/bin/python3
"""Module lists all states in database"""


import MySQLdb
import sys


def list_states():
    """ Lists all the states """
    
    # # connect to database
    # db = MySQLdb.connect(
    #     host='localhost',
    #     port=3306,
    #     user=sys.argv[1],
    #     passwd=sys.argv[2],
    #     db=sys.argv[3]
    # )

    # # Create cursor
    # cur = db.cursor()
    
    # # Execute query
    # cur.execute("SELECT * FROM states ORDER BY id")
    # rows = cur.fetchall()
    with MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    ) as db:
        cur = db.cursor()
        
        cur.execute("SELECT * FROM states ORDER BY id")
        rows = cur.fetchall()
        for row in rows:
            print(row)

if __name__ == "__main__":
    list_states()