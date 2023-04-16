#!/usr/bin/python3
# script that lists all states from the database hbtn_0e_0_usa

def getStates(userName, passWord, dbnName):
    """
    Accesses the database hbtn_0e_0_usa and grabs the states, then puts in ascending order.
    ARGS:
        username: the username
        password: the password
        dbName: the name of the databse to access
    """

    import MySQLdb

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=userName,
        passwd=passWord,
        db=dbName,
        charset="utf8"
    )

    cur = db.cursor()
    cur.execute("SELECT states FROM hbtn_0e_0_usa ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    # Close all cursors
    cur.close()

    # Close all databases
    db.close()

if __name__ == "__main__":
    """ Take in arguments and passes to get states from db """
    from sys import argv

    getStates(argv[1], argv[2], argv[3])