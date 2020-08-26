from test import PosDB
from test import setting
#ローカル用のurl
url = setting.setting_url

def getData(command):
    db = PosDB.PosDB(url)
    db.set_cursor()
    data = db.select_command(command)
    db.close()

    return data

def insertData(command):
    db = PosDB.PosDB(url)
    db.set_cursor()
    db.insert_command(command)


    db.close()
    return 0


def listQuestions(id,limit):
    sql = "SELECT * FROM questions ORDER BY ID DESC limit "+ str(limit) + "OFFSET " + str((id-1) * 3)
    data = getData(sql)
    count = getData("SELECT count(*) from questions")

    return data,count[0]["count"]






