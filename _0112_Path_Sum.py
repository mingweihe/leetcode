# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: return False
        return self.helper(root, 0, sum)

    def helper(self, node, cnt, sum):
        if not node.left and not node.right: return node.val + cnt == sum
        if node.right and self.helper(node.right, node.val + cnt, sum): return True
        if node.left and self.helper(node.left, node.val + cnt, sum): return True
        return False
