class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        ## Approach 2, one pass stack
        stack = []
        for i, x in enumerate(prices):
            while stack and prices[stack[-1]] >= x:
                prices[stack.pop()] -= x
            stack.append(i)
        return prices

        ## Approach 1
        # n, res = len(prices), []
        # for i in xrange(n):
        #     idx = i
        #     for j in xrange(i+1, n):
        #         if prices[j] <= prices[i]:
        #             idx = j
        #             break
        #     if idx == i: res += prices[i],
        #     else: res += prices[i] - prices[j],
        # return res
