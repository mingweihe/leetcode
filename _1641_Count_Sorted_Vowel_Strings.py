class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        to find the pattern
        n\k 1 2 3  4  5
            1 3 6  10 15
            1 4 10 20 35
            ...
        """
        dp = [0] + [1] * 5
        for i in xrange(n):
            for j in xrange(1, 6):
                dp[j] += dp[j-1]
        return dp[-1]
