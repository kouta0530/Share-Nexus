from test import PosDB
import datetime
import os
from test import setting

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
    sql = "SELECT * FROM questions ORDER BY ID DESC limit "+ str(limit) + "OFFSET " + str((id-1) * 5)
    data = getData(sql)
    count = getData("SELECT count(*) from questions")

    return data,count[0]["count"]


def uploadQuestion(title,text):
    sql = "INSERT INTO questions (title,text) VALUES('%s','%s')" %(title,text)
    insertData(sql)

def uploadAnswer(title,text,question_id):
    date = "2020-8-28"
    sql = "INSERT INTO answer(date,text,question_id,title) VALUES('%s','%s',%s,'%s')" %(date,text,question_id,title)
    insertData(sql)



