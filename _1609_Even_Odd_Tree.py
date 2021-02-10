# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(node, level):
            if not node: return
            dfs(node.left, level + 1)
            if level & 1 == 0:
                if node.val & 1 == 0 or node.val <= (d[level] or [float('-inf')])[-1]:
                    self.res = False
                    return
            else:
                if node.val & 1 or node.val >= (d[level] or [float('inf')])[-1]:
                    self.res = False
                    return
            d[level] += node.val,
            dfs(node.right, level + 1)
        self.res = True
        d = defaultdict(list)
        dfs(root, 0)
        return self.res
