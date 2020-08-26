#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 
#  FileName     : bibao.py
#  Date         : 2020年06月27日
#  Description  : 
# 

def func():
    a=1
    print("func")
    
    def func1(num):
        sum=num*a
        print(sum)
        print("func1")
    return func1()
v=func()
v(3)
