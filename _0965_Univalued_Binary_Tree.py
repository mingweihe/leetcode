# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # Approach 3
        def dfs(node):
            return not node or node.val == root.val \
                   and dfs(node.left) and dfs(node.right)

        return dfs(root)

        # Approach 2 interation(in order)
        # unival = root.val
        # stack, node = [], root
        # while stack or node:
        #     while node:
        #         stack.append(node)
        #         node = node.left
        #     node = stack.pop()
        #     if node.val != unival: return False
        #     node = node.right
        # return True

        # Approach 1 recursion
        # if not root: return True
        # cur_val = root.val
        # if root.left and root.left.val != cur_val: return False
        # if root.right and root.right.val != cur_val: return False
        # left_res = self.isUnivalTree(root.left)
        # right_res = self.isUnivalTree(root.right)
        # return left_res and right_res
