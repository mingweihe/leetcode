# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        # Approach 2
        if not root: return root
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if not root.left and not root.right and root.val == target:
            return None
        return root

        # Approach 1
        # def dfs(node, p):
        #     if not node: return node
        #     dfs(node.left, node)
        #     dfs(node.right, node)
        #     if not node.left and not node.right and node.val == target:
        #         if p:
        #             if p.left is node: p.left = None
        #             else: p.right = None
        # dfs(root, None)
        # if not root.left and not root.right and root.val == target:
        #     return None
        # return root
