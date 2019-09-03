# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = root.val

        def dfs(node):
            if not node: return 0
            max_left = dfs(node.left)
            max_right = dfs(node.right)
            self.res = max(self.res, max_left+max_right+node.val)
            maxi = max(max_left, max_right)
            # returning non-negative value is a good practice,
            # which avoids more cases' check
            return max(node.val + maxi, 0)
        dfs(root)
        return self.res
