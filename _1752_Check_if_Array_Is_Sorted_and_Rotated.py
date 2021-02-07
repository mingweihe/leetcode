class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt = 0
        for i in xrange(1, len(nums)):
            if nums[i] < nums[i-1]: cnt += 1
        if nums[0] < nums[-1]: cnt += 1
        return cnt <= 1
