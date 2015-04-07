#-*- coding: utf-8 -*-

from lib import *


class Solution:
    def minDepth(self, root):
        if root is None:
            return 0

        if root.left is not None and root.right is not None:
            lnodes = self.minDepth(root.left)
            rnodes = self.minDepth(root.right)
            return min(lnodes, rnodes) + 1

        if root.left is None and root.right is None:
            return 1

        if root.left is None and root.right is not None:
            return self.minDepth(root.right) + 1

        if root.left is not None and root.right is None:
            return self.minDepth(root.left) + 1
