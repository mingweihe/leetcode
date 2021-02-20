class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        for i in xrange(len(s)-1):
            for j in xrange(i+1, len(s)):
                cur = set(s[i:j+1])
                nice = True
                for c in cur:
                    if c.upper() not in cur or c.lower() not in cur:
                        nice = False
                        break
                if nice and j - i + 1 > len(res):
                    res = s[i:j+1]
        return res
