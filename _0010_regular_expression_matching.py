class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Method 2
        len_s, len_p = len(s), len(p)
        dp = [[False]*(len_p+1) for _ in xrange(len_s+1)]
        dp[0][0] = True
        for i in xrange(len_p):
            if p[i] == '*' and dp[0][i-1]:
                dp[0][i+1] = True
        for i in xrange(len_s):
            for j in xrange(len_p):
                if s[i] == p[j]:
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == '.':
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == '*':
                    if p[j-1] != s[i] and p[j-1] != '.':
                        dp[i+1][j+1] = dp[i+1][j-1]
                    else:
                        # dp[i][j] = dp[i][j-1] -> in the case a* counts as a single a
                        # dp[i][j] = dp[i-1][j] -> in the case a* counts as multiple a
                        # dp[i][j] = dp[i-2][j] -> in the case a* counts as empty
                        dp[i+1][j+1] = dp[i+1][j] or dp[i][j+1] or dp[i+1][j-1]
                # other cases are false
        return dp[len_s][len_p]
        # Method 1
        # return re.match('^{}$'.format(p), s)
