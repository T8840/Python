#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 
#  FileName     : linked_list.py
#  Date         : 2020年05月29日
#  Description  : 
# 

class Node:
    def __init__(self, value=None,next=None):
        self.value = value
        self.next = next
    def __str__(self):
        """用于调试"""
        return '<Node: value: {}, next = {}>'.format(self.value, self.next)

    __repr__ = __str__


class LinkedList:
    """
    链接表 ADT
    [root] -> [node0] -> [node1] -> [node2]
    """

    def __init__(self, maxsize=None):
        """
        :param maxsiez : int or None ,如果是None，无限扩充
        """
        self.maxsize = maxsize
        self.root = Node() # 默认root节点指向Node
        self.tailnode = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):
        if self.maxsize is not None and len(self) >= self.maxize:
            raise Exception('LinkedList is Full')
        node = Node(value) # 构造节点
        tailnode = self.tailnode
        if tailnode is None: 
            # 还没有append过， length = 0 ，追加到root后
            self.root.next = node
        else:
            # 否则追加到最后一个节点的后边，并更新最后一个节点是append的节点
            tailnode.next = node
        self.tailnode = node
        self.length +=1

    def appendleft(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('Linked is Full')
        node = Node(value)
        if self.tailnode is None:
            self.tailnode = node
        
        headnode = self.root.next
        self.root.next = node
        node.next = headnode
        self.length +=1

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node(self):
        """遍历从head节点 到tail节点"""
        curnode = self.root.next
        while curnode is not self.tailnode:
            # 从第一个节点开始遍历
            yield curnode
            curnode = curnode.next 
            # 移动到下一个节点
        if curnode is not None:
            yield curnode

def test_linked_list():
    ll = LinkedList()
    ll.append(0)
    ll.append(1)
    ll.append(2)
    ll.append(3)

    assert len(ll) == 4

def test_linked_list_append():
    ll = LinkedList()
    ll.appendleft(1)
    ll.append(2)
    assert list(ll) == [1,2]

if __name__=="__main__":
    test_linked_list()
    test_linked_list_append()

