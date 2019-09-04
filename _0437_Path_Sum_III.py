# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        d = {0: 1}
        self.count = 0
        self.helper(root, sum, 0, d)
        return self.count

    def helper(self, node, target, pathSum, d):
        if node:
            pathSum += node.val
            self.count += d.get(pathSum - target, 0)
            d[pathSum] = d.get(pathSum, 0) + 1
            self.helper(node.left, target, pathSum, d)
            self.helper(node.right, target, pathSum, d)
            d[pathSum] -= 1
