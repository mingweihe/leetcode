# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        stack = []
        self.helper(root, stack, res)
        return res

    def helper(self, root, stack, res):
        if not root: return;
        stack.append(root.val)
        self.helper(root.left, stack, res)
        if not root.left and not root.right: res.append('->'.join(map(str, stack)))
        self.helper(root.right, stack, res)
        stack.pop()
