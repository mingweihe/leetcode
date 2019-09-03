# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        hl = self.height(root.left, 0)
        hr = self.height(root.right, 0)
        if abs(hl - hr) > 1: return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, node, depth):
        if not node: return depth
        return max(self.height(node.left, depth + 1), self.height(node.right, depth + 1))