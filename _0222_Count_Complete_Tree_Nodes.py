# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        depth_left = self.depth(root, True)
        depth_right = self.depth(root, False)
        if depth_left == depth_right:
            return (1 << depth_left) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def depth(self, node, is_left):
        if not node: return 0
        if is_left: return self.depth(node.left, is_left) + 1
        return self.depth(node.right, is_left) + 1
