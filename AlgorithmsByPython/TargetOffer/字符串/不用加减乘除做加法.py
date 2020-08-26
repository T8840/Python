#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 
#  FileName     : 不用加减乘除做加法.py
#  Date         : 2020年06月29日
#  Description  : 写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。 
#                 思路参考：https://zhuanlan.zhihu.com/p/64642722
# 


# 方法1
class Solution:
    # 方法1
    def Add(self, num1, num2):
        while num2:
            result = (num1 ^ num2) & 0xffffffff
            carry = ((num1 & num2 ) << 1) & 0xffffffff
            num1 = result
            carry = carry
        if num1 <= 0x7fffffff:
            result = num1
        else:
            result = -((num1 -1) ^ 0xffffffff)
        return result    
    
    # 方法2
    def Add2(self, num1, num2):
        import ctypes
        a = ctypes.c_int32(num1).value
        b = ctypes.c_int32(num2).value
        while b !=0:
            carry = ctypes.c_int32(a & b).value
            a = ctypes.c_int32(a ^ b).value
            b = ctypes.c_int32(carry << 1).value
        return a 
    

def test():
    s = Solution()
    num1 = [5,7]
    # print(s.Add1(*num1))
    print(s.Add2(*num1))


test()
