class Solution(object):
    def minCost(self, houses, cost, m, n, target):
        """
        :type houses: List[int]
        :type cost: List[List[int]]
        :type m: int
        :type n: int
        :type target: int
        :rtype: int
        """
        dp = [[[float('inf')]*(n+1) for _ in xrange(target+1)] for _ in xrange(m+1)]
        for i in xrange(n+1): dp[0][0][i] = 0
        for i in xrange(1, m+1):
            for j in xrange(1, target+1):
                if houses[i-1] == 0:
                    for k in xrange(1, n+1):
                        for u in xrange(1, n+1):
                            if k == u:
                                dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][k] + cost[i-1][k-1])
                            else:
                                dp[i][j][k] = min(dp[i][j][k], dp[i-1][j-1][u] + cost[i-1][k-1])
                else:
                    k = houses[i-1]
                    for u in xrange(1, n+1):
                        if k == u:
                            dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][k])
                        else:
                            dp[i][j][k] = min(dp[i][j][k], dp[i-1][j-1][u])
        res = min(dp[m][target])
        return -1 if res == float('inf') else res
