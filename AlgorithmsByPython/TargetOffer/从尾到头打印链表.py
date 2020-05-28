#!/usr/bin/env python
# -*- coding: utf-8 -*- 
 # 
 #  FileName     : 从尾到头打印链表.py
 #  Date         : 2020年05月27日
 #  Description  : 输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
 # 
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    def printListFromTailToHead(self,listNode):
        l = []
        while listNode:
            l.append(listNode.val)
            listNode = listNode.next
        return l[::-1]

    def printListFromTailToHead2(self,listNode):
        pass


if __name__=="__main__":
    s = Solution()
    print(s.printListFromTailToHead())

