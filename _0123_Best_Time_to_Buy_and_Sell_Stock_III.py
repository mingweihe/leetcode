class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        l = len(prices)
        dp = [[0]*l for i in range(3)]
        for i in range(1, 3):
            maxDiff = -prices[0]
            for j in range(l):
                dp[i][j] = max(dp[i][j-1], maxDiff + prices[j])
                maxDiff = max(maxDiff, dp[i-1][j] - prices[j])
        return dp[2][l-1]
