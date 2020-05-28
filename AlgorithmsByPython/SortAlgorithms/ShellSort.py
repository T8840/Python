#!/usr/bin/env python
# -*- coding: utf-8 -*- 
 # 
 #  FileName     : ShellSort.py
 #  Date         : 2020年05月27日
 #  Description  : 希尔排序 
 # 
def shellSort(arr):
    subarrcount = len(arr)//2
    while subarrcount >0:
        for startposition in range(subarrcount):
            gapInsertionSort(arr,startposition,subarrcount)
        subarrcount = subarrcount//2
    return arr

def gapInsertionSort(arr,start,gap):
    for i in range(start+gap,len(arr), gap):
        position = i
        currentValue = arr[i]
        while ((position >= gap) and (arr[positon-gap] > currentValue)):
            arr[position] = arr[position-gap]
            position = position - gap
        arr[position] = currentValue

arr= [23,123,343,343,53,34,5345,343]
# print(shellSort(arr))


def shellSort2(arr):
    import math
    gap=1
    while (gap< int(math.floor(len(arr)/3))):
        gap = gap*3 +1
    while gap >0:
        for i in range(gap ,len(arr)):
            temp = arr[i]
            j = i - gap
            while j >=0 and arr[j] > temp:
                arr[j+gap] = arr[j]
                j-=gap
            arr[j+gap] = temp
        gap = int(math.floor(gap/3))
    return arr

print(shellSort2(arr))
