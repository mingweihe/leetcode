class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Approach 2 math, find patterns, time O(n)
        # 2 = 1 * 1
        # 3 = 2 * 1
        # 4 = 2 * 2
        # 5 = 3 * 2
        # 6 = 3 * 3
        # 7 = 3 * 4
        # 8 = 3 * 3 * 2
        # 9 = 3 * 3 * 3
        # 10 = 3 * 3 * 4
        if n < 4: return n - 1
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        return res * n

        # Approach 1 dynamic programming, time O(n^2)
        # dp = [0] * (n+1)
        # for i in xrange(2, n+1):
        #     for j in xrange(1, i):
        #         dp[i] = max(dp[i], max(j, dp[j]) * max(i-j, dp[i-j]))
        # return dp[-1]
