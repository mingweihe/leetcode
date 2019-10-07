class Solution(object):
    def isValidPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        n = len(s)
        dp = [[0] * n for _ in xrange(n)]
        for i in xrange(n-1, -1, -1):
            dp[i][i] = 1
            for j in xrange(i+1, n):
                if s[i] == s[j]: dp[i][j] = dp[i+1][j-1] + 2
                else: dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return n - dp[0][n-1] <= k
