class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs: return 0
        L = len(costs)
        dp = [[0]*3 for _ in xrange(L)]
        dp[0][:] = costs[0]
        for i in xrange(1, L):
            dp[i][0] = min(dp[i-1][1], dp[i-1][2])+costs[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2])+costs[i][1]
            dp[i][2] = min(dp[i-1][0], dp[i-1][1])+costs[i][2]
        return min(dp[-1])
