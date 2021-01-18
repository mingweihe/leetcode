# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        A = []
        def in_order(node):
            if not node: return
            in_order(node.left)
            A.append(node.val)
            in_order(node.right)
            
        def build(l, r):
            if l > r: return None
            mid = l + (r-l) / 2
            node = TreeNode(A[mid])
            node.left = build(l, mid-1)
            node.right = build(mid+1, r)
            return node
        
        in_order(root)
        return build(0, len(A)-1)
