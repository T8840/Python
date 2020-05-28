#!/usr/bin/env python
# -*- coding: utf-8 -*- 
 # 
 #  FileName     : BubbleSort.py
 #  Date         : 2020年05月27日
 #  Description  : 冒泡排序 
 # 

def bubbleSort(list):
    for i in range(len(list)):
        for j in range(i,len(list)):
            if list[i] >list[j]:
                list[i],list[j] = list[j], list[i]
    return list


list=[3,2,343,543,45,6,4,3]
print(bubbleSort(list))


# 改进冒泡排序：加入校验，在某次循环发现没有发生数值交换，直接跳出循环
def checkBubbleSort(list):
    exchange = True
    passnum = len(list) -1 
    while passnum >=1 and exchange:
        exchange = False
        for i in range(passnum):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1] , list[i]
                exchange = True
        passnum -= 1
    return list

print(checkBubbleSort(list))

# 冒泡排序优化：当某次冒泡操作已经没有数据交换时，说明已经达到完全有序，不用再继续执行后续冒泡操作。

def modiBubbleSort(list):
    # 提前退出冒泡循环的标志位
    for i in range(len(list)):
        flag = False
        for j in range(len(list) - i -1):
            if list[j] >list[j+1]:
                list[j],list[j+1] = list[j+1], list[j]
                flag = True
        if ( not flag):
            print("已经达到完全有序，不再执行后续操作！当前是第%d轮排序"%(i+1))
            break 
    return list
print(modiBubbleSort([21,3,4,5,73,34]))
print(modiBubbleSort([34,22,3,4,5,73,34]))
print(modiBubbleSort(list))
