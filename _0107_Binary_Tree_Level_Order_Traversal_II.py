# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def countDepth(node):
            if not node: return 0
            else: return 1 + max(countDepth(node.left), countDepth(node.right))
        depth = countDepth(root)
        res = [[] for _ in range(depth)]
        
        def helper(node, level):
            if node:
                helper(node.left, level - 1)
                helper(node.right, level - 1)
                res[level].append(node.val)
        helper(root, depth - 1)
        return res
