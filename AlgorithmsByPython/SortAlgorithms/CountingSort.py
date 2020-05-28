#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 
#  FileName     : CountingSort.py
#  Date         : 2020年05月28日
#  Description  : 计数排序 
# 

def countingSort(arr):
    
    maxNum = max(arr)
    minNum = min(arr)
    length = maxNum - minNum +1
    # 以最大值和最小值的差作为中间数组的长度，并构建中间数组tempArr，元素的值初始化为0
    tempArr = [0 for i in range(length)]
    resArr = list(range(len(arr)))
    # 第一次遍历：遍历arr每个元素，统计每个元素的出现次数存入中间数组（下标是arr中的元素值，值是该元素在arr中出现的次数）
    for num  in arr:
        tempArr[num - minNum] +=1
    # 第二次遍历：遍历中间数组，每个位置的值=当前值 + 前一个位置的值，用来统计出小于等于当前下标的元素个数
    for j in range(1,length):
        tempArr[j] = tempArr[j]+tempArr[j-1]
    # 第三次遍历：反向遍历arr的每个元素，找到该元素值在中间数组的对应下标，以这个中间数组的值作为结果数组的下标，将该元素存入结果数组    
    for i in range(len(arr) -1, -1 ,-1):
        resArr[tempArr[arr[i] - minNum] -1] = arr[i]
        tempArr[arr[i] - minNum] -= 1
    return resArr


arr = [12,343,121,3436,23,32432,23,215,657]
print(countingSort(arr))
