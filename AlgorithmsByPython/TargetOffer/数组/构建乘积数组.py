#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 
#  FileName     : 构建乘积数组.py
#  Date         : 2020年06月29日
#  Description  : 给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
#                 （注意：规定B[0] = A[1] * A[2] * ... * A[n-1]，B[n-1] = A[0] * A[1] * ... * A[n-2];）
# 

class Solution:
    def multiply(self,A):
        B = []
        count = 0
        for i in range(len(A)):
            m=1
            for j in range(len(A)):
                if j != count:
                    m *= A[j]
            B.append(m)
            count +=1
        return B

   
def test():
    A1=[1,2,3,4,5]
    A2=[3,2,1]
    A3=[0,2,4,6]
    s = Solution()
    print(s.multiply(A1))
    print(s.multiply(A2))
    print(s.multiply(A3))


test()
