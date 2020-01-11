# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def add(node, dis_to_des):
            if not node: return
            if dis_to_des == 0:
                self.res += node.val
                return
            add(node.left, dis_to_des - 1)
            add(node.right, dis_to_des - 1)

        def dfs(node):
            if not node: return
            if node.val & 1 == 0:
                add(node, 2)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.res
