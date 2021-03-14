class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        d = [i for i in xrange(len(s1)) if s1[i] != s2[i]]
        if len(d) > 2 or len(d) == 1: return False
        return not d or s1[d[0]] == s2[d[1]] and s1[d[1]] == s2[d[0]]
