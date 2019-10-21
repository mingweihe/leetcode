# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # Approach 2 post-order traversal
        def sub_rob(node):
            if not node: return 0, 0
            left = sub_rob(node.left)
            right = sub_rob(node.right)
            rob13 = node.val + left[0] + right[0]
            rob2 = max(left) + max(right)
            return rob2, rob13

        return max(sub_rob(root))

        # Approach 1 time O(h^6) - TLE
        # if not root: return 0
        # res = root.val
        # if root.left: res += self.rob(root.left.left) + self.rob(root.left.right)
        # if root.right: res += self.rob(root.right.left) + self.rob(root.right.right)
        # return max(res, self.rob(root.left)+self.rob(root.right))
