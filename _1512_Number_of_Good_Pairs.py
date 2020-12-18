class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in xrange(len(nums)-1):
            for j in xrange(i+1, len(nums)):
                res += nums[i] == nums[j]
        return res
