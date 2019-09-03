# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        # Approach 1 dynamic programming
        if n == 0: return []
        dp = [[] for _ in xrange(n + 1)]
        dp[0].append(None)
        for i in xrange(1, n + 1):
            for j in xrange(i):
                lefts = dp[j]
                rights = dp[i - j - 1]
                for left in lefts:
                    for right in rights:
                        root = TreeNode(j + 1)
                        root.left = left
                        root.right = self.clone(right, j + 1)
                        dp[i].append(root)
        return dp[n]
        # Approach 2 dfs
        # if n == 0: return []
        # return self.helper(1, n)

    def helper(self, start, end):
        res = []
        if start > end:
            res.append(None)
        for i in xrange(start, end + 1):
            lefts = self.helper(start, i - 1)
            rights = self.helper(i + 1, end)
            for left in lefts:
                for right in rights:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    res.append(root)
        return res

    def clone(self, node, k):
        if not node: return node
        root = TreeNode(node.val + k)
        root.left = self.clone(node.left, k)
        root.right = self.clone(node.right, k)
        return root