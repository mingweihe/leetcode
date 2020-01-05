class Solution(object):
    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        # Approach 2, conciser
        M = 10 ** 9 + 7
        dp = [0, 1]
        for i in xrange(steps):
            dp[1:] = [sum(dp[j-1:j+2]) % M for j in xrange(1, min(arrLen+1, steps-i+1, i+3))]
        return dp[1] % M

        # Approach 1, less memory cost, faster
        # M = 10 ** 9 + 7
        # dp = [0] * arrLen
        # dp[0] = 1
        # for i in xrange(steps):
        #     last = 0
        #     for j in xrange(min(arrLen, steps - i, i + 2)):
        #         temp = dp[j]
        #         next_ = dp[j + 1] if j + 1 < arrLen else 0
        #         dp[j] = (last + dp[j] + next_) % M
        #         last = temp
        # return dp[0] % M
