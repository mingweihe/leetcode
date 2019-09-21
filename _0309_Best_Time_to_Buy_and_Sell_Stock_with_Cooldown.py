class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
            Three states transition
            hold: from rest or hold
            sold: from hold
            rest: from rest or sold
        """
        # Approach 2 time O(n), space O(1)
        hold, sold, rest = -float('inf'), 0, 0
        for x in prices:
            t = hold
            hold = max(hold, rest - x)
            rest = max(rest, sold)
            sold = t + x
        return max(sold, rest)

        # Approach 1 time O(n), space O(n)
        # L = len(prices)+1
        # holds, solds, rests = [0]*L, [0]*L, [0]*L
        # holds[0] = -float('inf')
        # for i in xrange(1, L):
        #     holds[i] = max(holds[i-1], rests[i-1]-prices[i-1])
        #     solds[i] = holds[i-1] + prices[i-1]
        #     rests[i] = max(rests[i-1], solds[i-1])
        # return max(rests[-1], solds[-1])
