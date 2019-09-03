# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        warning number zero!! so we should better use node
        instead of value
        """

        # Approach 3 recursion max, pre-order, min variable
        def helper(node, minn, maxi):
            if not node: return True
            if minn and node.val <= minn.val: return False
            if maxi and node.val >= maxi.val: return False
            return helper(node.left, minn, node) and helper(node.right, node, maxi)

        return helper(root, None, None)

        # Approach 2 recursion in-order:
        # warning number 0
        # keyword: global previous node variable
        # self.pre = None
        # def dfs(node):
        #     if not node: return True
        #     if not dfs(node.left): return False
        #     if self.pre and self.pre.val >= node.val: return False
        #     self.pre = node
        #     return dfs(node.right)
        # return dfs(root)

        # Approach 1 iteration in-order
        # if not root: return True
        # stack, node = [], root
        # last = -float('inf')
        # while stack or node:
        #     while node:
        #         stack.append(node)
        #         node = node.left
        #     node = stack.pop()
        #     if last >= node.val: return False
        #     last = node.val
        #     node = node.right
        # return True
