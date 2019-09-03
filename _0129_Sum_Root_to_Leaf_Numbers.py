# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def dfs(node, summ):
            if not node: return
            summ = summ*10 + node.val
            if not node.left and not node.right:
                self.res += summ
                return
            dfs(node.left, summ)
            dfs(node.right, summ)
        dfs(root, 0)
        return self.res
