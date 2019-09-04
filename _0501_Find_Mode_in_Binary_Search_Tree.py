# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        self.mode = [root.val]
        self.num = self.numberOfOccred(root, root.val)
        self.helper(root.left, root.val)
        self.helper(root.right, root.val)
        return self.mode

    # any kinds of traverse
    def helper(self, node, N):
        if not node: return
        if node.val != N:
            n = self.numberOfOccred(node, node.val)
            if n > self.num:
                self.num = n
                self.mode = [node.val]
            if n == self.num and not node.val in self.mode:
                self.mode.append(node.val)
        self.helper(node.left, node.val)
        self.helper(node.right, node.val)

    # count number of a val from a subtree
    def numberOfOccred(self, node, N):
        if not node: return 0
        return int(node.val == N) + self.numberOfOccred(node.left, N) + self.numberOfOccred(node.right, N)

