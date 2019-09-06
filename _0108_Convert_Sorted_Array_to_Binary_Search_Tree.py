# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return None
        left = 0
        right = len(nums) - 1
        mid = (left + right) >> 1
        root = TreeNode(nums[mid])
        root.left = self.helper(nums, left, mid - 1)
        root.right = self.helper(nums, mid + 1, right)
        return root

    def helper(self, arr, l, r):
        if l <= r:
            m = (l + r) >> 1
            node = TreeNode(arr[m])
            node.left = self.helper(arr, l, m - 1)
            node.right = self.helper(arr, m + 1, r)
            return node
