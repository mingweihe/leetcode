# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxSumBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node.left and not node.right:
                self.res = max(self.res, node.val)
                return True, node.val, node.val, node.val
            
            is_BST_left, summ_left, min_left, max_left = True, 0, node.val, node.val
            is_BST_right, summ_right, min_right, max_right = True, 0, node.val, node.val
            
            if node.left:
                is_BST_left, summ_left, min_left, max_left = dfs(node.left)
                
            if node.right:
                is_BST_right, summ_right, min_right, max_right = dfs(node.right)
                
            if is_BST_left and is_BST_right:
                if (not node.left or max_left < node.val) and (not node.right or node.val < min_right):
                    cur_sum = summ_left + summ_right + node.val
                    self.res = max(self.res, cur_sum)
                    return True, cur_sum, min_left, max_right
                else:
                    return False, 0, 0, 0
            else:
                return False, 0, 0, 0
            
        self.res = 0
        dfs(root)
        return self.res
    