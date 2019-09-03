# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Approach 2
        res = []
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited: res.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return res
        # Approach 1
        # if not root: return []
        # res = []
        # stack = []
        # node = root
        # while stack or node:
        #     while node:
        #         stack.append(node)
        #         node = node.left
        #     node = stack[-1].right
        #     if not node:
        #         res.append(stack.pop().val)
        #     else:
        #         stack[-1].right = None
        # return res
