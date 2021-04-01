# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Approach 2, one pass
        def dfs(node, lb, rb):
            if not node: return
            if lb: ans.append(node.val)
            if not lb and not rb and not node.left and not node.right:
                ans.append(node.val)
            dfs(node.left, lb, rb and not node.right)
            dfs(node.right, lb and not node.left, rb)
            if rb: ans.append(node.val)
        ans = [root.val]
        dfs(root.left, True, False)
        dfs(root.right, False, True)
        return ans
    
        # # Approach 1, slightly more than 1 pass
        # ans = [root.val]
        # node = root.left
        # while node:
        #     if node.left:
        #         ans += node.val,
        #         node = node.left
        #     elif node.right:
        #         ans += node.val,
        #         node = node.right
        #     else: break
        # def dfs(node):
        #     if not node.left and not node.right:
        #         if node != root:
        #             ans.append(node.val)
        #         return
        #     if node.left: dfs(node.left)
        #     if node.right: dfs(node.right)
        # dfs(root)
        # rights = []
        # node = root.right
        # while node:
        #     if node.right:
        #         rights += node.val,
        #         node = node.right
        #     elif node.left:
        #         rights += node.val,
        #         node = node.left
        #     else: break
        # return ans + rights[::-1]
