#-*- coding: utf-8 -*-

# 递归深度遍历整个树，并且在参数中带上从根到当前节点的数据总和，当碰到叶子节点的时候，将和放入一个队列中


from lib import *


class Solution:
    def __init__(self):
        self.vals = []

    def hasPathSum(self, root, ssum):
        self.deepFind(root, 0)
        if ssum in self.vals:
            return True
        return False

    def deepFind(self, root, father_num):
        if root is None:
            return
        if root.left is None and root.right is None:
            self.vals.append(father_num + root.val)
            return
        if root.left is not None:
            self.deepFind(root.left, father_num + root.val)
        if root.right is not None:
            self.deepFind(root.right, father_num + root.val)
        

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    s = Solution()
    print s.hasPathSum(root, 22)
    print s.vals
