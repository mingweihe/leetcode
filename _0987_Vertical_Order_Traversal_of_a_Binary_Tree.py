# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def dfs(node, data, X, Y):
            if not node: return
            data.append([X, -Y, node.val])
            dfs(node.left, data, X-1, Y-1)
            dfs(node.right, data, X+1, Y-1)
            
        data = []
        dfs(root, data, 0, 0)
        data.sort()
        data.append([float('inf'), 0, 0])
        res, cur = [], []
        last_X = float('-inf')
        for x, y, val in data:
            if x != last_X:
                if cur: res.append(cur)
                cur = [val]
            else:
                cur.append(val)
            last_X = x
        return res
