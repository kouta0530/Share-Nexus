from flask import render_template,request,session,redirect,url_for 
from test import app
from test import models
from test import setting

import math
import os


#app.secret_key = setting.secret_key
app.secret_key = os.environ["SECRET_KEY"]

@app.route("/",methods = ["GET"])
def toppages():
    error = session.get("error")
    
    return render_template("top.html",error=error)


@app.route("/post",methods =["POST"])
def post_problem():
    problem = request.form["problem"]

    if(problem == ""):
        error = "問題文を貼り付けてください"
        session["error"] = error
        return redirect(url_for("toppages"))

    session.pop("error",None)
    explanation = {
        "text":problem,
        "urls":"https://",
    }

    return render_template("explanation.html",explanation = explanation)

    #return redirect(url_for("explanation"))

@app.route("/explanation")
def explanation():
    explanation = {
        "text":request.form["problem"],
        "urls":"https://",
    }

    return render_template("explanation.html",explanation = explanation)


@app.route("/index")
@app.route("/index/page=<int:id>")
def index(id = 1):
    data,count = models.listQuestions(id,5)

    return render_template("index.html",data = data,count = math.ceil(count / 5))

@app.route("/upload",methods = ["POST"])
def upload():
    text = request.form["text"]
    title = request.form["title"]
    #title = "No title"
    models.uploadQuestion(title,text)

    return redirect("/index")

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

