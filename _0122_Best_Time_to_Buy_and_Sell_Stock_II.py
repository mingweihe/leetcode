class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Approach 1
        res = 0
        for i in range(1, len(prices)):
            res += max(prices[i] - prices[i-1], 0)
        return res

        # Approach 2
        if not prices or len(prices) == 1: return 0
        res = curP =0
        buy = prices[0]
        for i in range(1, len(prices)):
            curP = max(curP, prices[i] - buy)
            if i < len(prices) - 1 and prices[i+1] < prices[i] and curP > 0:
                res += curP
                buy = prices[i+1]
                curP = 0
            else:
                buy = min(buy, prices[i])
        res += curP
        return res
