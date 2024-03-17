class Solution(object):
    def countSubstrings(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: int
        """
        res = 0
        cnt = s.count(c)
        for i in xrange(cnt):
            res += i+1
        return res
