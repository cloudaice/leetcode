#-*- coding: utf-8 -*-


from lib import *


class Solution:
    def sortedArrayToBST(self, num):
        l = len(num)
        if l == 0:
            return None
        if l == 1:
            return TreeNode(num[0])
        mid = l / 2
        node = TreeNode(num[mid])
        node.left = self.sortedArrayToBST(num[:mid])
        node.right = self.sortedArrayToBST(num[mid + 1:])
        return node

if __name__ == "__main__":
    s = Solution()
    print s.sortedArrayToBST([1, 2, 3, 4, 5])
