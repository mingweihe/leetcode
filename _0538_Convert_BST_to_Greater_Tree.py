# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.prev = 0

        def helper(node):
            if not node: return
            helper(node.right)
            self.prev = node.val = node.val+self.prev
            helper(node.left)
        helper(root)
        return root
