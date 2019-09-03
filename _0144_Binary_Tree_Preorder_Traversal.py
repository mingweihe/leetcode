# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Approach 1
        if not root: return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        return res
        # Approach 2
        # if not root: return []
        # res = []
        # stack = []
        # while root:
        #     res.append(root.val)
        #     stack.append(root)
        #     root = root.left
        # while stack:
        #     node = stack.pop().right
        #     while node:
        #         res.append(node.val)
        #         stack.append(node)
        #         node = node.left
        # return res




