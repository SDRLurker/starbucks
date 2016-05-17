#!/usr/bin/python
# -*- coding: utf-8 -*-

class Node(object):
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

"""
 Check if linked list has cycle
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return 0 if no cycle else return 1
"""

def HasCycle(head):
    tortoise = head
    hare = head
    while hare != None:
        hare = hare.next
        if hare == None:
            return 0
        hare = hare.next
        tortoise = tortoise.next
        if tortoise == hare:
            return 1
    return 0

one = Node(1)
print HasCycle(one)
two_1 = Node(1)
two_2 = Node(2)
two_3 = Node(3)
two_1.next = two_2
two_2.next = two_3
two_3.next = two_2
print HasCycle(two_1)
