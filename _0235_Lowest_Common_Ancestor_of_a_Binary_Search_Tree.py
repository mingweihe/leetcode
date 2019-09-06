# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Approach 2
        n = root
        if p.val > q.val:
            t = p
            p = q
            q = t
        while n:
            if p.val <= n.val <= q.val: return n
            if n.val < p.val:
                n = n.right
            else:
                n = n.left

        # Approach 1
    #     if q.val < p.val: return self.helper(root, q, p)
    #     return self.helper(root, p, q)
    #
    # def helper(self, root, p, q):
    #     if p.val <= root.val <= q.val: return root
    #     if root.val < p.val: return self.lowestCommonAncestor(root.right, p, q)
    #     return self.lowestCommonAncestor(root.left, p, q)
