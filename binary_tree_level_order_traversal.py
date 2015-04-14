#-*- coding: utf-8 -*-


from lib import *


class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if root is None:
            return []
        queue = [root]
        level = 1
        rst = [[root.val]]
        while True:
            thisLevel = []
            for i in range(level):
                node = queue[0]
                queue = queue[1:]
                if node.left is not None:
                    queue.append(node.left)
                    thisLevel.append(node.left.val)
                if node.right is not None:
                    queue.append(node.right)
                    thisLevel.append(node.right.val)
            level = len(thisLevel)
            if level == 0:
                break
            rst.append(thisLevel)
        return rst

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    s = Solution()
    print s.levelOrder(root)
