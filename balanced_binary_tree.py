#-*- coding: utf-8 -*-

from lib import *


class Solution:
    def __init__(self):
        self.isBalance = True

    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root is None:
            return True
        leftDepth = self.dep(root.left)
        rightDepth = self.dep(root.right)
        if abs(leftDepth - rightDepth) > 1:
            self.isBalance = self.isBalance and False
        else:
            self.isBalance = self.isBalance and True
        return self.isBalance

    def dep(self, root):
        if root is None:
            return 0
        l = self.dep(root.left)
        r = self.dep(root.right)
        d = max(l, r) + 1
        if abs(l - r) > 1:
            self.isBalance = self.isBalance and False
        else:
            self.isBalance = self.isBalance and True
        return d
