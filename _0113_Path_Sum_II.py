# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        backtracking in a binary tree
        """
        res = []
        self.helper(res, [], root, sum)
        return res

    def helper(self, res, curL, node, remained):
        if not node: return
        curL.append(node.val)
        if not node.left and not node.right:
            if remained == node.val:
                res.append(list(curL))
        self.helper(res, curL, node.left, remained - node.val)
        self.helper(res, curL, node.right, remained - node.val)
        curL.pop()
