# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        n = [root]
        res = []
        while n:
            t = []
            s = 0
            cnt = 0
            while n:
                cur = n.pop()
                if cur.left: t.append(cur.left)
                if cur.right: t.append(cur.right)
                s += cur.val
                cnt += 1
            n.extend(t)
            res.append(s/float(cnt))
        return res
