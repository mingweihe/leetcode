"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        # Approach 2
        res = []
        if not root: return res
        q = [root]
        while q:
            arr4res = []
            arr4q = []
            for n in q:
                arr4res.append(n.val)
                for i in n.children: arr4q.append(i)
            q = arr4q
            res.append(arr4res)
        return res

        # Approach 1
        #         res = []
        #         self.helper(root, res, 0)
        #         return res

        #     def helper(self, node, res, depth):
        #         if node:
        #             if len(res) <= depth: res.append([node.val])
        #             else: res[depth].append(node.val)
        #             for n in node.children: self.helper(n, res, depth+1)
