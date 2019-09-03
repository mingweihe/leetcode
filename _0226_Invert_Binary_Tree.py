# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Approach 1 recursion
        if not root: return root
        right = self.invertTree(root.right)
        root.right = self.invertTree(root.left)
        root.left = right
        return root

        # Approach 2 iteration
        # if not root: return root
        # s = [root]
        # while s:
        #     n = s.pop()
        #     t = n.left
        #     n.left = n.right
        #     n.right = t
        #     if n.left: s.append(n.left)
        #     if n.right: s.append(n.right)
        # return root
