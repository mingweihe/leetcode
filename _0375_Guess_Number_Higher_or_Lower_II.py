class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
            dynamic programming
        """
        # Approach 2 iteration + dp
        dp = [[0] * (n+1) for _ in xrange(n+1)]
        for i in xrange(n-1, -1, -1):
            for j in xrange(i+1, n+1):
                val = float('inf')
                for x in xrange(i, j):
                    val = min(val, max(dp[i][x-1], dp[x+1][j]) + x)
                dp[i][j] = val
        return dp[1][n]

        # Approach 1 recursion + dp
        # dp = [[0] * (n+1) for _ in xrange(n+1)]
        # def helper(i, j):
        #     if i >= j: return 0
        #     if dp[i][j] != 0: return dp[i][j]
        #     res = float('inf')
        #     for x in xrange(i, j+1):
        #         res = min(res, max(helper(i, x-1), helper(x+1, j)) + x)
        #     dp[i][j] = res
        #     return res
        # return helper(1, n)
