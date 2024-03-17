class Solution(object):
    def isSubstringPresent(self, s):
        """
        :type s: str
        :rtype: bool
        """
        rs, L = s[::-1], len(s)
        for i in xrange(L-1):
            if s[i:i+2] in rs: return True
        return False
