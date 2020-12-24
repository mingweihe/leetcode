# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countPairs(self, root, distance):
        """
        :type root: TreeNode
        :type distance: int
        :rtype: int
        """
        res = [0]
        def dfs(node, depth, stats):
            if not node.left and not node.right:
                stats += depth,
                return
            left, right = [], []
            if node.left:
                dfs(node.left, depth+1, left)
            if node.right:
                dfs(node.right, depth+1, right)
            if left and right:
                for i in left:
                    for j in right:
                        cur = i + j - 2 * depth
                        if cur <= distance:
                            res[0] += 1
            stats += left
            stats += right
        dfs(root, 0, [])
        return res[0]
