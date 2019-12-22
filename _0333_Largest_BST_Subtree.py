# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node):
            if not node: return 0, float('inf'), float('-inf')
            sL, minL, maxL = helper(node.left)
            sR, minR, maxR = helper(node.right)
            if -1 in (sL, sR): return -1, 0, 0
            if node.val <= maxL or node.val >= minR: return -1, 0, 0
            ans = sL + sR + 1
            self.res = max(self.res, ans)
            return ans, min(minL, node.val), max(maxR, node.val)
        self.res = 0
        helper(root)
        return self.res
