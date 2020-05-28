#!/usr/bin/env python
# -*- coding: utf-8 -*- 
 # 
 #  FileName     : SelectionSort.py
 #  Date         : 2020年05月27日
 #  Description  : 选择排序 
 # 
#  
def selectionSort(arr):
    for i in range(len(arr)-1):
        minIndex = i
        for j in range(i+1,len(arr)):
            if arr[minIndex]>arr[j]:
               minIndex = j
        if i!=minIndex:       
            arr[i] ,arr[minIndex] = arr[minIndex] ,arr[i]
    return arr

print(selectionSort([3,7,5,1,2,6,4]))
print(selectionSort([3,24,33]))
