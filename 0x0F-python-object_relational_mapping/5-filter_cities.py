#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_4_usa """
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         port=3306)
    cursor = db.cursor()
    match = sys.argv[4]
    cursor.execute("""SELECT cities.name FROM cities INNER JOIN states
                    ON states.id=cities.state_id WHERE states.name=%s""",
                    (match,))
    result = cursor.fetchall()
    results = [i[0] for i in result]
    print(', '.join(results))

    cursor.close()
    db.close()
