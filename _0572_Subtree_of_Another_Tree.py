# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s: return False
        if self.sameTree(s, t): return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def sameTree(self, a, b):
        if not a and not b: return True
        if not a and b: return False
        if a and not b: return False
        if a.val != b.val: return False
        return self.sameTree(a.left, b.left) and self.sameTree(a.right, b.right)
