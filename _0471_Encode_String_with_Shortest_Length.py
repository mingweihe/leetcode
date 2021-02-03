class Solution(object):
    def encode(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [[''] * n for _ in xrange(n)]
        for i in xrange(n-1, -1, -1):
            for j in xrange(i, n):
                cur_str = s[i:j+1]
                dp[i][j] = cur_str
                if len(cur_str) < 5: continue
                for k in xrange(i, j):
                    prev = dp[i][k] + dp[k+1][j]
                    if len(prev) < len(dp[i][j]):
                        dp[i][j] = prev
                for k in xrange(1, len(cur_str)/2+1):
                    pattern = cur_str[:k]
                    if len(cur_str) % k == 0 and not cur_str.replace(pattern, ''):
                        cur = str(len(cur_str) / k) + '[' + dp[i][i+k-1] + ']'
                        if len(cur) < len(dp[i][j]):
                            dp[i][j] = cur
        return dp[0][n-1]
