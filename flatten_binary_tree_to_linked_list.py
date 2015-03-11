#-*- coding: utf-8 -*-


from lib import *


class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root is None:
            return
        l = []
        l.append(root)
        ptr = TreeNode(0)
        while len(l) > 0:
            node = l.pop()
            ptr.right = node
            ptr.left = None
            ptr = node
            if node.right is not None:
                l.append(node.right)
            if node.left is not None:
                l.append(node.left)


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    s.flatten(root)
    while root is not None:
        print root.val, root.left
        root = root.right
