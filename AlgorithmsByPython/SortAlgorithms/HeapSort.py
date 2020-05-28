#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 
#  FileName     : HeapSort.py
#  Date         : 2020年05月28日
#  Description  : 堆排序 
# 

def heapSort(arr):
    if arr == None or len(arr) == 0:
        return

    length = len(arr)
    output = []
    for i in range(length):
        tempLen = len(arr)
        for j in range(tempLen//2 -1, -1 , -1):
            preIndex = j
            preVal, heap = arr[preIndex], False
            while 2 * preIndex < tempLen -1 and not heap:
                curIndex = 2 * preIndex +1
                if curIndex < tempLen -1:
                    if arr[curIndex] < arr[curIndex + 1]:
                        curIndex +=1
                if preVal >=arr[curIndex]:
                    heap = True
                else:
                    arr[preIndex] = arr[curIndex]
                    preIndex = curIndex
                
            arr[preIndex] = preVal
        output.insert(0,arr.pop(0))
    return output


arr = [23,234,343,22,31,2,34]
print(heapSort(arr))
    
