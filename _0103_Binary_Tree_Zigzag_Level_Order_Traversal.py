from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        use a queue to hold values and their order
        remember this simple deque is from collections package
        """
        if not root: return []
        res, queue = [], deque([root])
        to_right = True
        while queue:
            layer = []
            for i in xrange(len(queue)):
                node = queue.popleft()
                if to_right:
                    layer.append(node.val)
                else:
                    layer.insert(0, node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            to_right = False if to_right else True
            res.append(layer)
        return res
