class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        if not p: return 0
        dp = [1] * (len(p))
        hist = {p[0]: 1}
        for i in xrange(1, len(p)):
            if (ord(p[i-1])-97 + 1) % 26 == ord(p[i]) - 97:
                dp[i] += dp[i-1]
            hist[p[i]] = max(hist.get(p[i], 0), dp[i])
        return sum(hist.values())
