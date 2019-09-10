class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k >= len(prices) / 2:
            return self.helper(prices)
        dp = [[0] * len(prices) for _ in xrange(k + 1)]
        for i in xrange(1, k + 1):
            # max of previous transaction with one buy
            tmp_map = -prices[0]
            for j in xrange(1, len(prices)):
                dp[i][j] = max(dp[i][j - 1], tmp_map + prices[j])
                tmp_map = max(tmp_map, dp[i - 1][j - 1] - prices[j])
        return dp[k][len(prices) - 1]

    def helper(self, prices):
        res = 0
        for i in xrange(1, len(prices)):
            res += max(0, prices[i] - prices[i - 1])
        return res
