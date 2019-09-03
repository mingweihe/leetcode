class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        dp typical problem
        time: O(n^2)
        space: O(n)
        """
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in xrange(1, n + 1):
            for j in xrange(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[n]
