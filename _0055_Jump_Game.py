class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maximum = 0
        for i in xrange(len(nums)):
            if i > maximum: return False
            maximum = max(maximum, i+nums[i])
        return True
