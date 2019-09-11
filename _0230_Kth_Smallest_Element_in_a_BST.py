# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.res = 0
        self.cnt = k

        def dfs(node):
            if not node: return
            dfs(node.left)
            self.cnt -= 1
            if self.cnt == 0:
                self.res = node.val
                return
            dfs(node.right)
        dfs(root)
        return self.res
