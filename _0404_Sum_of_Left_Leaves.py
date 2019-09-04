# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root, imleft=None):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        if not root.left and not root.right and imleft == True: return root.val
        return self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right, False)
