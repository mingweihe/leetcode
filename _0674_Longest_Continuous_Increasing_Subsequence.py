class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, cnt = 0, 0
        for i in xrange(len(nums)):
            if i == 0 or nums[i] > nums[i-1]:
                cnt += 1
            else:
                cnt = 1
            res = max(res, cnt)
        return res
