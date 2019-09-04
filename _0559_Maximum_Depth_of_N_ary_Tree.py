# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        self.res = 0

        def dfs(node, depth):
            if not node: return
            depth += 1
            self.res = max(self.res, depth)
            for n in node.children: dfs(n, depth)
        dfs(root, 0)
        return self.res
