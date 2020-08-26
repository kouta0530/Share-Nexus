from flask import render_template,request,session,redirect,url_for
from test import app
from test import models
import math

@app.route("/")
@app.route("/page=<int:id>")
def index(id = 1):
    data,count = models.listQuestions(id,3)

    return render_template("test.html",data = data,count = math.ceil(count / 3))

@app.route("/upload",methods = ["POST"])
def upload():
    text = request.form["text"]
    title = request.form["title"]
    userID = session["sessionID"]
    models.uploadQuestion(title,text,userID)

    return render_template("index.html")

@app.route("/question/<int:id>")
def show(id):
    sql = "select * from questions where id =" + str(id)
    data = models.getData(sql)
    return render_template("question.html",data = data[0])

@app.route("/answer",methods=["POST"])
def answer():
    question_id = request.form["id"]
    text = request.form["text"]
    userID = request.form["sessionID"]
    redirect_url = "/question/".join(str(question_id))

    models.uploadAnswer(question_id,text,userID)

    return redirect(redirect_url)
    
