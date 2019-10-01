class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        stack with backward traversal
        time O(n) space O(n)
        """
        stack = []
        mid = float('-inf')
        for i in xrange(len(nums)-1, -1, -1):
            if nums[i] < mid: return True
            else:
                while stack and nums[i] > stack[-1]:
                    mid = stack.pop()
                stack.append(nums[i])
        return False
