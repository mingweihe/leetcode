class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        anti case of using two pointer:
        s1 -> ab
        s2 -> bd
        s3 -> abdb
        so we use dp to solve this problem
        """
        L1, L2, L3 = len(s1), len(s2), len(s3)
        if L1 + L2 != L3: return False
        dp = [[False]*(L2+1) for _ in xrange(L1+1)]
        dp[0][0] = True
        for i in xrange(1, L1+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for i in xrange(1, L2+1):
            dp[0][i] = dp[0][i-1] and s2[i-1] == s3[i-1]
        for i in xrange(1, L1+1):
            for j in xrange(1, L2+1):
                dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1] \
                    or dp[i][j-1] and s2[j-1] == s3[i+j-1]
        return dp[L1][L2]
