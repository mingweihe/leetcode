class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        l = len(nums)
        dp = [0]*(l+1)
        dp[1] = nums[0]
        for i in range(2, l+1):
            dp[i] = max(nums[i-1] + dp[i-2], dp[i-1])
        return dp[l]
