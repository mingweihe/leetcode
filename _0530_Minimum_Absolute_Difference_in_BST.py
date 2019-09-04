# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        a = []

        def helper(node):
            if not node: return
            helper(node.left)
            a.append(node.val)
            helper(node.right)

        helper(root)
        res = a[1] - a[0]
        for i in range(2, len(a)): res = min(res, a[i] - a[i - 1])
        return res
