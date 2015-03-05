#-*- coding: utf-8 -*-


from lib import *


class Solution:
    def __init__(self):
        self.l = []

    def inorderTraversal(self, root):
        if root is None:
            return self.l
        self.inorderTraversal(root.left)
        self.l.append(root.val)
        self.inorderTraversal(root.right)
        return self.l
