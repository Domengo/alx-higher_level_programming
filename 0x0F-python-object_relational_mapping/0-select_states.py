#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
            user="root", passwd="Dicklongflop?7", db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    db.close()
