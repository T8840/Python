#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 
#  FileName     : demo.py
#  Date         : 2020年05月30日
#  Description  : 



import flask

app = flask.Flask(__name__) 

@app.route("/")
def demo():
    return 'hello!'


app.run(host="0.0.0.0",port=8000)
