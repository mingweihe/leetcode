class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
            1 dimensional dp solution problem
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
            else dp[i] = False
        """
        L = len(s)
        sets = set(wordDict)
        dp = [False]*(L+1)
        dp[0] = True
        for i in xrange(1, L+1):
            for j in xrange(i):
                if dp[j] and s[j:i] in sets:
                    dp[i] = True
                    break
        return dp[-1]
