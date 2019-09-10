# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Approach 2 bfs
        res, queue = [], []
        if root: queue.append(root)
        while queue:
            for i in xrange(len(queue)):
                node = queue.pop(0)
                if i == 0: res.append(node.val)
                if node.right: queue.append(node.right)
                if node.left: queue.append(node.left)
        return res

        # Approach 1 dfs
        # res = []
        # def dfs(res, node, lvl):
        #     if node is None: return
        #     if len(res) == lvl: res.append(node.val)
        #     dfs(res, node.right, lvl+1)
        #     dfs(res, node.left, lvl+1)
        # dfs(res, root, 0)
        # return res
