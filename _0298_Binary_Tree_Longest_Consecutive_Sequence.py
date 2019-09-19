# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Approach 2 pre order
        if not root: return 0

        def pre_order(node, cur_max, target):
            if not node: return
            if node.val == target:
                cur_max += 1
            else:
                cur_max = 1
            self.res = max(self.res, cur_max)
            pre_order(node.left, cur_max, node.val + 1)
            pre_order(node.right, cur_max, node.val + 1)

        self.res = 0
        pre_order(root, 0, root.val)
        return self.res

        # Approach 1 post order
        # def post_order(node):
        #     if not node: return 0
        #     left = post_order(node.left)
        #     right = post_order(node.right)
        #     cur_max = 1
        #     if left and node.val == node.left.val - 1:
        #         cur_max = max(cur_max, left+1)
        #     if right and node.val == node.right.val - 1:
        #         cur_max = max(cur_max, right+1)
        #     self.res = max(self.res, cur_max)
        #     return cur_max
        # self.res = 0
        # post_order(root)
        # return self.res
