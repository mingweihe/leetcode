# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        keyword:
            self.pre
            self.first
            self.second
        """
        if not root: return

        def dfs(node):
            if not node: return
            dfs(node.left)
            if self.prev and self.prev.val >= node.val:
                if not self.first: self.first = self.prev
                self.second = node
            self.prev = node
            dfs(node.right)
        self.prev = self.first = self.second = None
        dfs(root)
        self.first.val, self.second.val = self.second.val, self.first.val
