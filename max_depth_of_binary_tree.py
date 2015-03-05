#-*- coding: utf-8 -*-


from lib import *


class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root is None:
            return 0
        dep = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        return dep
