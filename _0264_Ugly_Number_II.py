class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ind1 = ind2 = ind3 = 0
        dp = [1]*n
        for i in xrange(1, n):
            n1 = dp[ind1] * 2
            n2 = dp[ind2] * 3
            n3 = dp[ind3] * 5
            dp[i] = min(n1, n2, n3)
            if dp[i] == n1: ind1 += 1
            if dp[i] == n2: ind2 += 1
            if dp[i] == n3: ind3 += 1
        return dp[-1]
