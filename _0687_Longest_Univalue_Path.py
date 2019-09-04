# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.calculate(root)
        return self.res

    def calculate(self, node):
        if not node: return 0
        leftL = self.calculate(node.left)
        rightL = self.calculate(node.right)
        curL, curR = 0, 0
        if node.left and node.left.val == node.val:
            curL = leftL + 1
        if node.right and node.right.val == node.val:
            curR = rightL + 1
        self.res = max(self.res, curL + curR)
        return max(curL, curR)
