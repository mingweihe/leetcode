class Solution(object):
    # def __init__(self):
    # instance variable will be gone after re-new a instance
    # self._dp = [0]

    # class / static variable
    _dp = [0]

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Approach 3 conciser
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i * i] for i in xrange(1, int(len(dp) ** .5) + 1)) + 1,
        return dp[n]

        # Approach 2 optimized with cache
        # for i in xrange(len(self._dp), n+1):
        #     mini = float('inf')
        #     for j in xrange(1, int(i**.5)+1):
        #         mini = min(mini, self._dp[i-j*j]+1)
        #     self._dp.append(mini)
        # return self._dp[n]

        # Approach 1
        # dp = [float('inf')] * (n+1)
        # dp[0] = 0
        # for i in xrange(1, n+1):
        #     for j in xrange(1, int(i**.5)+1):
        #         dp[i] = min(dp[i], dp[i-j*j]+1)
        # return dp[-1]
