# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root: return []
        stack, res = [root], []
        while stack:
            n = stack.pop()
            res.append(n.val)
            if n.children: stack.extend([i for i in n.children])
        return res[::-1]
