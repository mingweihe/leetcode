class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        dynamic programming
        s[i-1] == t[j-1]: dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
        s[i-1] != t[j-1]: dp[i][j] = dp[i-1][j]
        """
        len_s, len_t = len(s), len(t)
        dp = [[0] * (len_t + 1) for _ in xrange(len_s + 1)]
        for i in xrange(len_s):
            dp[i][0] = 1
        for i in xrange(1, len_s + 1):
            for j in xrange(1, len_t + 1):
                if s[i - 1] != t[j - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
        return dp[len_s][len_t]
