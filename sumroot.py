#-*- coding: utf-8 -*-


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        total = []

        def middleFind(n, node):
            print n, node.val
            if node is None:
                return
            if node.left is None and node.right is None:
                total.append(n * 10 + node.val)
            if node.left is not None:
                middleFind(n * 10 + node.val, node.left)
            if node.right is not None:
                middleFind(n * 10 + node.val, node.right)

        middleFind(0, root)
        return sum(total)

if __name__ == "__main__":
    Root = TreeNode(6)
    Root.left = TreeNode(8)
    Root.left.left = TreeNode(7)
    Root.left.right = TreeNode(3)
    Root.left.left.right = TreeNode(8)
    solution = Solution()
    print solution.sumNumbers(Root)
