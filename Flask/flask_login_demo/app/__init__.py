#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 
#  FileName     : app.py
#  Date         : 2020年06月19日
#  Description  : 
# 
import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)

from flask import Flask, Blueprint, render_template
from config import Config
from app.forms import LoginForm
app = Flask(__name__)
app.config.from_object(Config)

auth = Blueprint('auth',__name__)


@auth.route('/')
def get():
    return "hello"

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title="Sign In", form=form)


if __name__=="__main__":
    app.run(host='0.0.0.0',port='8000',debug=True)
