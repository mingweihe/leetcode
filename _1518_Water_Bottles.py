class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        res = numBottles
        while numBottles >= numExchange:
            a, b = divmod(numBottles, numExchange)
            res += a
            numBottles = a + b
        return res
