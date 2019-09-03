class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1: return 0
        buy = prices[0]
        res = 0
        for i in range(1, len(prices)):
            res = max(res, prices[i] - buy)
            buy = min(buy, prices[i])
        return res
