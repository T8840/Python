#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 
#  FileName     : RadixSort.py
#  Date         : 2020年05月28日
#  Description  : 基数排序。基数排序分为：最高位优先（Most Significant Digit First) 与最低位优先法（Least Significant Digit First) 
# 

# 最低位优先法
def radixSortLSD(list):
    if len(list) == 0:
        return
    if len(list) == 1:
        return list
    tempList = list
    maxNum = max(list)
    radix = 10
    while maxNum * 10 > radix:
        newArr = [ [],[],[],[],[],[],[],[],[],[] ]
        for n1 in tempList:
            testnum = n1 % radix
            testnum = testnum // (radix /10)
            for n2 in range(10):
                if testnum ==n2:
                    newArr[n2].append(n1)
        tempList=[]
        for i in range(len(newArr)):
            for j in range(len(newArr[i])):
                tempList.append(newArr[i][j])
        radix *=10
    return tempList


list= [12,34,2,33,123,346,85,32]
print(radixSortLSD(list))

