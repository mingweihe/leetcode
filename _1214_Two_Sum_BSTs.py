import bisect


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def twoSumBSTs(self, root1, root2, target):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :type target: int
        :rtype: bool
            bisect time O(n*log(n))
        """
        if not root1 or not root2: return False

        def to_array(node):
            stack = []
            res = []
            while stack or node:
                while node:
                    stack.append(node)
                    node = node.left
                node = stack.pop()
                res.append(node.val)
                node = node.right
            return res

        arr1, arr2 = to_array(root1), to_array(root2)
        n = len(arr2)
        for num in arr1:
            t = target - num
            ind = bisect.bisect(arr2, t)
            if arr2[ind - 1] == t:
                return True
        return False
