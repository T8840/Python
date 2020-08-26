#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 
#  FileName     : DoubleLinkList.py
#  Date         : 2020年05月29日
#  Description  : 双向链表 
# 

from ./SingleLinkList.py import SingleLinkList
class Node(object):
    def __init__(self,elem):
        self.elem = elem
        self.pre = None
        self.next = None

class DoubleLinkList(SingleLinkList):

    def length(self):
        """打印链表的节点数"""
        """使用游标cur，如果游标的next指向none，那么就终止循环"""
        cur = self.__head
        count = 0
        while cur != None:
            count +=1
            cur = cur.next
        return count

    def add(self,item):
        """在头部添加元素item"""
        """使用游标cur,本来游标指向头部，如果头部有元素，那么头部之前的元素要往后移，新头部为item，item所在的node指向之前的头部"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            self.__head = node 
            self.__head.next = cur
        
    def append(self,item):
        """在尾部添加"""
        """使用游标cur,游标初始指向头部，如果游标的下一个节点不为None，游标往后移动直到游标的下一个节点为None，此时将游标的值，item所在的node指向之前的头部"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node     
        
    def travel(self):
        """遍历链表，打印链表的所有节点值"""
        cur = self.__head
        # 为了方便查看，将所有的元素写入到一个临时列表中
        tmp = []
        while cur != None:
            #print(cur.elem)
            tmp.append(cur.elem)
            cur = cur.next
        print(tmp)

    def find(self):
        """查找"""
        pass

    def remove(self):
        """删除指定值,删除时使用2个游标，pre与cur"""
        pass

def test_normal_link():
    node = Node(100)
    single_obj = SingleLinkList(node)
    print(single_obj.length())
    print(single_obj.is_empty())
    single_obj.travel()
    
    single_obj.append(5)
    single_obj.append(6)
    single_obj.append(7)
    single_obj.travel()

    single_obj.add(3)
    single_obj.travel()

def test_empty_link():
    single_obj = SingleLinkList()
    print(single_obj.length())
    print(single_obj.is_empty())
    single_obj.add(1)
    single_obj.travel()
    single_obj.append(5)
    single_obj.travel()
    single_obj.add(3)
    single_obj.travel()

if __name__ =="__main__":
    test_normal_link()
    test_empty_link()

