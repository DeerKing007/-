#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 14:35
# @Author  : hbw
# @Site    : 
# @File    : 单链表.py
# @Software: PyCharm
# 节点对象
class Node(object):
    def __init__(self,item):
        self.item=item
        self.head=None
        self.tail=None

#　单链表
class Lianbiao(object):
    def __init__(self):
        self.root=None

    def add(self,item):
        node=Node(item)
        if not self.root:
            self.root=node
            return
        q=[self.root]
        while q:
            c_node=q.pop()
            #print(c_node.item)
            if not c_node.tail:
                c_node.tail=node
                return
            q.append(c_node.tail)
    def bianli(self):
        q=[self.root]
        while True:
            node=q.pop()
            if not node:
                break
            print(node.item)
            q.append(node.tail)
if __name__ == '__main__':
    l=Lianbiao()
    for i in range(10):
        l.add(i)
    l.bianli()
