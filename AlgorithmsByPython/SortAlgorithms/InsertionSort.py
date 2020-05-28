#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 
#  FileName     : InsertionSort.py
#  Date         : 2020年05月28日
#  Description  : 插入排序
# 

def insertionSort(list):
    for key,item in enumerate(list):
        index = key
        while index > 0 and list[index -1] >item:
            list[index] = list[index-1]
            index -=1
        list[index] = item
    return list
list=[21,23,45,62,3,2,33,4,26]
print(insertionSort(list))


# 优化
def insertionSort2(list):
    for index in range(1,len(list)):
        currentvalue=list[index]
        position = index

        while position >0 and list[position -1 ] > currentvalue:
            list[position] = list[position -1]
            position -=1
        list[position] = currentvalue

    return list

print(insertionSort2(list))
