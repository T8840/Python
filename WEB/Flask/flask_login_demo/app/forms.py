#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 
#  FileName     : form.py
#  Date         : 2020年06月19日
#  Description  : 
# 

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField 
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('User Name', validators = [DataRequired()])
    password = PasswordField('Password',validators = [DataRequired()] )
    remember_me = BooleanField('remember me', default = False)
