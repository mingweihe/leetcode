class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or s == '' or s == '0': return 0
        l=len(s)
        if l == 1: return 1
        dp = [0]*(l+1)
        dp[0] = 1
        if s[0] != '0': dp[1] = 1
        for i in range(2, l+1):
            curNum = int(s[i-2:i])
            if 10 < curNum < 27 and curNum != 20:
                dp[i] = dp[i-1] + dp[i-2]
            elif 0 < curNum%10 < 10:
                dp[i] = dp[i-1]
            elif curNum in (10, 20):
                dp[i] = dp[i-2]
        return dp[l]
