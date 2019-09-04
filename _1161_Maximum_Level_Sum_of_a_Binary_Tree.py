# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 1
        stack = [root]
        res = 1
        cur_lvl = 1
        maximum = -float('inf')
        while stack:
            layer = []
            summ = 0
            while stack:
                node = stack.pop()
                summ += node.val
                if node.left:
                    layer.append(node.left)
                if node.right:
                    layer.append(node.right)
            if summ > maximum:
                res = cur_lvl
                maximum = summ
            stack = layer
            cur_lvl += 1
        return res
