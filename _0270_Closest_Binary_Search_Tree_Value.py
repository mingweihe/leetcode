# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """

        # Approach 3 recursion time O(log(n))
        def dfs(node, t, res):
            if not node: return res
            if abs(node.val - t) < abs(res - t): res = node.val
            if t > node.val:
                res = dfs(node.right, t, res)
            else:
                res = dfs(node.left, t, res)
            return res

        return dfs(root, target, root.val)

        # Approach 2 iteration time O(log(n))
        # res = root.val
        # while root:
        #     if abs(root.val-target) < abs(res-target): res = root.val
        #     root = root.left if root.val > target else root.right
        # return res

        # Approach 1 recursion time O(n)
        # if not root: return float('inf')
        # left = self.closestValue(root.left, target)
        # if abs(target-left) < abs(target-root.val): return left
        # right = self.closestValue(root.right, target)
        # if abs(target-right) < abs(target-root.val): return right
        # return root.val
