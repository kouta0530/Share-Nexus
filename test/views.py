from flask import render_template,request,session,redirect,url_for
from test import app
from test import models

@app.route("/")
def index():
    
    return "hello"