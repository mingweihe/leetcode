# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
            take advantage of the feature of BST
        """
        # Approach 2 iteration
        candidate = None
        while root:
            if root.val <= p.val:
                root = root.right
            else:
                candidate = root
                root = root.left
        return candidate

        # Approach 1 recursion
        # if not root: return None
        # if root.val <= p.val:
        #     return self.inorderSuccessor(root.right, p)
        # left = self.inorderSuccessor(root.left, p)
        # return left if left else root
