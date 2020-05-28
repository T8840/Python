#!/usr/bin/env python
# -*- coding: utf-8 -*- 
 # 
 #  FileName     : QuickSort.py
 #  Date         : 2020年05月27日
 #  Description  : 快速排序 
 # 

def quickSort(arr):

    if len(arr) <2:
        return arr
    else:
        privot = arr[0]
        less = [ i for i in arr[1:] if i<=privot ]
        greater = [ i for i in arr[1:] if i> privot ]
        return quickSort(less) + [privot] + quickSort(greater)

arr = [ 12,3,34,21,343,253,42 ]
print(quickSort(arr))
