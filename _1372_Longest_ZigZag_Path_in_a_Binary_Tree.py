# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def dfs(node, direction, length):
            if not node: return
            self.res = max(self.res, length)
            if node.left:
                cur_length = 1 if direction else length + 1
                dfs(node.left, True, cur_length)
            if node.right:
                cur_length = 1 if not direction else length + 1
                dfs(node.right, False, cur_length)
        dfs(root.left, True, 1)
        dfs(root.right, False, 1)
        return self.res
