class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
            medium level dynamic programming
            time O(n^3) space O(n^2)
            dp calculations must start from short to long segment
        """
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0]*(n+2) for _ in xrange(n+2)]
        for l in xrange(1, n+1):
            for i in xrange(1, n-l+2):
                j = i + l - 1
                for k in xrange(i, j+1):
                    dp[i][j] = max(dp[i][j],
                        dp[i][k-1] + nums[i-1]*nums[k]*nums[j+1] + dp[k+1][j])
        return dp[1][n]
