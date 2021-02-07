class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = float('-inf')
        accum = 0
        mini = maxi = 0
        for x in nums:
            accum += x
            ans = max(ans, abs(accum - mini), abs(accum - maxi))
            mini = min(mini, accum)
            maxi = max(maxi, accum)
        return ans
