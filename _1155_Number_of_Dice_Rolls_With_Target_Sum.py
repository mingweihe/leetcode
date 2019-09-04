class Solution(object):
    def numRollsToTarget(self, d, f, target, res = 0):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        math
        """
        # Bottom-Up DP approach
        dp = [0]*(target+1)
        dp[0] = 1
        for i in xrange(d):
            dp1 = [0]*(target+1)
            for j in xrange(1, f+1):
                for k in xrange(j, target+1):
                    dp1[k] += dp[k-j]
                    # dp1[k] %= 1000000007
            dp, dp1 = dp1, dp
        return dp[target] % 1000000007
