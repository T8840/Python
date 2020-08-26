#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# * 
# *  FileName     : 替换空格.py
# *  Date         : 2020年05月27日
# *  Description  : 请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。 
# *

class Solution:
    def replaceSpace(self, s):
        list = []
        for i in s:
            if i == ' ': 
                i='%20'
            list.append(i)
        return ''.join(list)

    def replaceSpace2(self,s):
        s.replace(" ","%20")
        return s

if __name__=="__main__":
    s=Solution()
    print(s.replaceSpace2('We are happy.'))
    print(s.replaceSpace2('hello world'))
