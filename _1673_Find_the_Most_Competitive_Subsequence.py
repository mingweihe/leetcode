class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        stack = []
        for i, x in enumerate(nums):
            while stack and x < stack[-1] and len(stack) - 1 + len(nums) - i >= k:
                stack.pop()
            if len(stack) < k:
                stack += x,
        return stack
