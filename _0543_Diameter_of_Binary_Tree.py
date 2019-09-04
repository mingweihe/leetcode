# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Approach 1
        self.res = 0

        def depth(node):
            if not node: return 0
            dL, dR = depth(node.left), depth(node.right)
            self.res = max(self.res, dL + dR)
            return max(dL, dR) + 1

        depth(root)
        return self.res
        # Approach 2
        # self.res = 0
        #
        # def depth(node, L):
        #     if not node: return L
        #     L += 1
        #     return max(depth(node.left, L), depth(node.right, L))
        #
        # def helper(node):
        #     if not node: return
        #     self.res = max(self.res, depth(node.left, 0) + depth(node.right, 0))
        #     helper(node.left)
        #     helper(node.right)
        #
        # helper(root)
        # return self.res
