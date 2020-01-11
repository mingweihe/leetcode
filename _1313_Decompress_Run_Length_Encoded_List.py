class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in xrange(0, len(nums), 2):
            res += nums[i]*[nums[i+1]]
        return res
