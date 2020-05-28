#!/usr/bin/env python
# -*- coding: utf-8 -*- 
 # 
 #  FileName     : MergeSort.py
 #  Date         : 2020年05月27日
 #  Description  : 归并排序 
 # 

def mergeSort(arr):
    if len(arr) >1:
        mid = len(arr) // 2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        
        i,j,k=0,0,0
        while i <len(lefthalf) and j <len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i += 1
            else:
                arr[k] = righthalf[j]
                j +=1
            k += 1

        while i <len(lefthalf):
            arr[k] = lefthalf[i]
            i +=1
            k +=1
        
        while j < len(righthalf):
            arr[k] = righthalf[j]
            j +=1
            k +=1

arr = [234,343,12,343,343,12,2314,3432]
mergeSort(arr)
print(arr)


def mergeSort2(arr):
    import math
    if (len(arr)<2):
        return arr
    middle = int(math.floor(len(arr)/2))
    left, right = arr[0:middle], arr[middle:]
    return merge(mergeSort2(left), mergeSort2(right))

def merge(left,right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0));
        else:
            result.append(right.pop(0))
        while left:
            result.append(left.pop(0))
        while right:
            result.append(right.pop(0))
        return result

print(mergeSort2(arr))
