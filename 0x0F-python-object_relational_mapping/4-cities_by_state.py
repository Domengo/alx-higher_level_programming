#!/usr/bin/python3
"""
Displays all values in the cities table of the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                     passwd=argv[2], db=argv[3])
cursor = db.cursor()
cursor.execute("SELECT * FROM cities ORDER BY id ASC")
results = cursor.fetchall()
for row in results:
    print(row)

db.close()
cursor.close()
