from test import PosDB
from test import setting
import datetime
import os

#ローカル用のurl
#url = setting.setting_url
url = os.environ["DATABASE_URL"]

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


def uploadQuestion(title,text):
    sql = "INSERT INTO questions (title,text) VALUES('%s','%s')" %(title,text)
    insertData(sql)

def uploadAnswer(question_id,text,userID):
    sql = 'INSERT INTO answer(title,date,text,userID) VALUES(%s,%s,%s)' %(question_id,text,userID)
    insertData(sql)



