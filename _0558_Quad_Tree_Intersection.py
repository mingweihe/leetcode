# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution(object):
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        if quadTree1.isLeaf: return quadTree1.val and quadTree1 or quadTree2
        if quadTree2.isLeaf: return quadTree2.val and quadTree2 or quadTree1
        tL = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        tR = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bL = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        bR = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
        if tL.isLeaf and tR.isLeaf and bL.isLeaf and bR.isLeaf and tL.val == tR.val == bL.val == bR.val:
            node = Node(tL.val, True, None, None, None, None)
        else:
            node = Node(False, False, tL, tR, bL, bR)
        return node
