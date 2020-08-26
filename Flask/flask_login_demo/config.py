#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 
#  FileName     : config.py
#  Date         : 2020年06月19日
#  Description  : 
# 


import os
basedir =os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABSE_URL') or 'sqlite:///' + os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False



