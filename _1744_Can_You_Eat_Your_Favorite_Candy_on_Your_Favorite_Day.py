class Solution(object):
    def canEat(self, candiesCount, queries):
        """
        :type candiesCount: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        def solve(A):
            ftype, fday, dailymax = A
            prev_total = accums[ftype]
            num_total = accums[ftype+1]     
            if num_total < fday + 1: return False
            return dailymax * (fday+1) > prev_total             
        accums = [0]
        for x in candiesCount:
            accums += accums[-1] + x,
        return map(solve, queries)
