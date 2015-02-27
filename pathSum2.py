#-*- coding: utf-8 -*-

# 与pathSum解题思路类似，只是参数中的和换成是一个list，保存了从根节点到当前节点的路径上的所有数据。


from lib import *


class Solution:
    def __init__(self):
        self.vals = []

    def pathSum(self, root, ssum):
        self.deepFind(root, [])
        result = []
        for items in self.vals:
            if sum(items) == ssum:
                result.append(items)
        return result

    def deepFind(self, root, l):
        if root is None:
            return
        if root.left is None and root.right is None:
            self.vals.append(l + [root.val])
        if root.left is not None:
            self.deepFind(root.left, l + [root.val])
        if root.right is not None:
            self.deepFind(root.right, l + [root.val])

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    s = Solution()
    print s.pathSum(root, 22)
    print s.vals
