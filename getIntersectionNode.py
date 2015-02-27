#-*- coding: utf-8 -*-

from lib import *


class Solution:
    def getIntersectionNode(self, headA, headB):
        a = self.getListLen(headA)
        b = self.getListLen(headB)
        nodea = headA
        nodeb = headB
        if a > b:
            for i in range(a - b):
                nodea = nodea.next
        if b > a:
            for i in range(b - a):
                nodeb = nodeb.next

        intersectionNode = None
        while nodea is not None:
            if nodea == nodeb:
                intersectionNode = nodea
                break
            nodea = nodea.next
            nodeb = nodeb.next
        return intersectionNode
    
    def getListLen(self, head):
        node = head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count
