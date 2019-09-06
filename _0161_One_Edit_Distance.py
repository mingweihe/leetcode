class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len_s, len_t = len(s), len(t)
        for i in xrange(min(len_s, len_t)):
            if s[i] != t[i]:
                if len_s == len_t:
                    return s[i+1:] == t[i+1:]
                elif len_s > len_t:
                    return s[i+1:] == t[i:]
                else:
                    return s[i:] == t[i+1:]
        return abs(len_s - len_t) == 1
