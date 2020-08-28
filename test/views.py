from flask import render_template,request,session,redirect,url_for 
from test import app
from test import models
#from test import setting

import math
import os


#app.secret_key = setting.secret_key
app.secret_key = os.environ["SECRET_KEY"]

@app.route("/",methods = ["GET"])
def toppages():
    error = session.get("error")
    data,count = models.listQuestions(1,5)
    return render_template("top.html",error=error,data=data)


@app.route("/post",methods =["POST"])
def post_problem():
    problem = request.form["problem"]

    if(problem == ""):
        error = "問題文を貼り付けてください"
        session["error"] = error
        return redirect(url_for("toppages"))

    session.pop("error",None)
    explanation = {
        "problem":problem,
        "text":["台形の公式","二次方程式",  "1.各点の座標や直線に注目する","2.どこを上底下底にするか考える"],
        "urls":["https://math.005net.com/yoten/2jihoBunsyo.php","https://math.005net.com/yoten/2jihoBunsyo.php?reidai=rei4"],
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
    return render_template("index.html",data = data,count = int(count / 5) + 1)

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
    answer_sql = "select * from answer where question_id = %s " %(id)
    data = models.getData(sql)
    answers = models.getData(answer_sql)

    return render_template("question.html",data = data[0],answers = answers)

@app.route("/answer",methods=["POST"])
def answer():
    text = request.form["text"]
    title = request.form["title"]
    question_id = request.form["id"]

    models.uploadAnswer(title,text,question_id)
    redirect_url = "/question/%s" %(str(question_id))


    return redirect(redirect_url) 

