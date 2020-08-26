from test import PosDB

def getList(command):
    db = PosDB.PosDB("")
    db.set_cursor()
    data = db.select_command(command)
    db.close()

    return data

def getData(id):
    data = id

    return data

def insertData(command):
    db = PosDB.PosDB("")
    db.set_cursor()
    db.insert_command(command)


    db.close()
    return 0



