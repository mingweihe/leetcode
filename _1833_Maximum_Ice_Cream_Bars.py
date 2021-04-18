class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        ans = 0
        for x in costs:
            if coins >= x:
                ans += 1
                coins -= x
        return ans
