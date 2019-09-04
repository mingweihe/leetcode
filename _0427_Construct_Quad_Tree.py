import numpy as np


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        root = None
        l = len(grid)
        g = np.array(grid)
        s = g.sum()
        root = Node(True, True, None, None, None, None)
        if s == l*l: return root
        elif s == 0:
            root.val = False
            return root
        root.isLeaf = False
        h=l//2
        root.topLeft = self.construct(g[:h, :h])
        root.topRight = self.construct(g[:h, h:])
        root.bottomLeft = self.construct(g[h:, :h])
        root.bottomRight = self.construct(g[h:, h:])
        return root
