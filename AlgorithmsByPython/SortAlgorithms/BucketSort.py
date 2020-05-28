#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 
#  FileName     : BucketSort.py
#  Date         : 2020年05月28日
#  Description  : 桶排序 
# 

def bucketSort(arr):
    max_len = max(arr) +1
    book = [0 for x in range(0, max_len)]
    for i in arr:
        book[i] +=1
    return [i for i in range(0,max_len)   for j in range(0, book[i])]   


arr = [223,343,324532,2342,212,124,3435]
print(bucketSort(arr))
