# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def sumForSubtree(node):
            if not node: return 0
            sumL = sumForSubtree(node.left)
            sumR = sumForSubtree(node.right)
            self.res += abs(sumL - sumR)
            return node.val + sumL + sumR

        sumForSubtree(root)
        return self.res
