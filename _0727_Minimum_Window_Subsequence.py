class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        m, n = len(S), len(T)
        dp = [[0] * (n+1) for _ in xrange(m+1)]
        
        for i in xrange(1, n+1):
            dp[0][i] = float('inf')
            
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if S[i-1] == T[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i-1][j] + 1
        
        min_len, idx = float('inf'), -1
        for i in xrange(1, m+1):
            if dp[i][n] < min_len:
                min_len = dp[i][n]
                idx = i-1
                
        if idx == -1: return ''
        return S[idx-min_len+1:idx+1]
