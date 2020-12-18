class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [0] + [1] * (n)
        for i in xrange(2, n+1):
            if i % 2 == 0: nums[i] = nums[i/2]
            else: nums[i] = nums[i/2] + nums[i/2+1]
        return max(nums)
