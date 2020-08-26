from flask import render_template,request,session,redirect,url_for
from test import app
from test import models

@app.route("/")
@app.route("/page=<int:id>")
def index(id = 0):
    return render_template("test.html",id = id)

@app.route("/upload",methods = ["POST"])
def upload():
    text = request.form["text"]
    sessionId = session["sessionId"]


    return render_template("index.html")

@app.route("/question/<int:id>")
def show(id):
    return str(id)
