# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None: return ""
        leftStr = self.tree2str(t.left)
        rightStr = self.tree2str(t.right)
        if t.left is None and t.right is None: return str(t.val)
        if t.right is None: return str(t.val) + '(' + leftStr + ')'
        return str(t.val) + '(' + leftStr + ')(' + rightStr + ')'
