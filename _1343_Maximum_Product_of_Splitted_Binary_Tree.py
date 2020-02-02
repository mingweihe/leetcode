# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        M = 10 ** 9 + 7
        self.sum = 0

        def dfs(node):
            if not node: return
            self.sum += node.val
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        self.diff = float('inf')
        self.a = 0

        def dfs(node):
            if not node: return 0
            sum_left = dfs(node.left)
            sum_right = dfs(node.right)
            diff_left = abs(self.sum - 2 * sum_left)
            if diff_left < self.diff:
                self.diff = diff_left
                self.a = sum_left
            diff_right = abs(self.sum - 2 * sum_right)
            if diff_right < self.diff:
                self.diff = diff_right
                self.a = sum_right
            return sum_left + sum_right + node.val

        dfs(root)
        return (self.sum - self.a) * self.a % M
