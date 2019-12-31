import heapq


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """

        def to_array(node, ans):
            if not node: return
            if node.left: to_array(node.left, ans)
            ans += node.val,
            if node.right: to_array(node.right, ans)

        arr1, arr2 = [], []
        to_array(root1, arr1)
        to_array(root2, arr2)
        # merge two sorted arrays approach 2, time O(m+n)
        return heapq.merge(arr1, arr2)
        # merge two sorted arrays approach 1, time O(n*log(n))
        # return sorted(arr1 + arr2)
