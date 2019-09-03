# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # Approach 2
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[:ind])
            root.right = self.buildTree(preorder, inorder[ind + 1:])
            return root
        # Approach 1
#         return self.helper(0, 0, len(preorder)-1, preorder, inorder)

#     def helper(self, prestart, instart, inend, preorder, inorder):
#         if prestart == len(preorder) or instart > inend: return None
#         node = TreeNode(preorder[prestart])
#         inindex = 0
#         for i in xrange(instart, inend+1):
#             if inorder[i] == preorder[prestart]:
#                 inindex = i
#                 break
#         node.left = self.helper(prestart+1, instart, inindex-1, preorder, inorder)
#         node.right = self.helper(prestart+inindex-instart+1,
#             inindex+1, inend, preorder, inorder)
#         return node
