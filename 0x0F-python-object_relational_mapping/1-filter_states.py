#!/usr/bin/python3
# script that lists all states with a name starting with N (upper N)
#from the database hbtn_0e_0_usa

def getStates(userName, passWord, dbName):
    """ Accesses the database hbtn_0e_usa and grabs states that begin with 'N'
    ARGS:
        userName: the username
        passWord: the password
        dbName: the name of the database to access
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
    cur.execute("SELECT * from states WHERE name LIKE BINARY 'N%'")
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    """Take in arguments and passes to get states from db"""
    from sys import argv

    getStates(argv[1], argv[2], argv[3])