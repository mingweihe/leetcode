# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Approach 2
        global res, pre  # self.res, self.pre is also a nice solution for nested scopes
        pre, res = float('-inf'), float('inf')

        def helper(node):
            global res, pre
            if not node: return
            helper(node.left)
            res = min(res, node.val - pre)
            pre = node.val
            helper(node.right)

        helper(root)
        return res

        # Approach 1
        # res, last = float('inf'), -float('inf')
        # stack, node = [], root
        # while stack or node:
        #     while node:
        #         stack.append(node)
        #         node=node.left
        #     node = stack.pop()
        #     res = min(res, node.val-last)
        #     last = node.val
        #     node = node.right
        # return res
