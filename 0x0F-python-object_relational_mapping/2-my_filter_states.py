#!/usr/bin/python3
#takes in an argument and displayes all values in the states table of
#htbn_0e_0_usa where name matches the argument

def getStates(userName, passWord, dbName, stateName):
    """Accesses database hbtn_0e_0_usa and grabs states that begin with 'N'.
    ARGS:
        username: the username
        passWord: the password
        dbName: the name of the database to access
        statename: the name of the state to check
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
    sqlCommand = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(stateName)
    cur.execute(sqlcommand)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()

    if __name__== "__main__":
        """ Take in arguments and passes to get states from db"""
        from sys import orig_argv

        getStates(argv[1], argv[2, [argv3], argv[4]])