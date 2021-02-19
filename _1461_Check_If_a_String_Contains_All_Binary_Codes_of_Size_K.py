class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        return len(set(s[i:i+k] for i in xrange(len(s)-k+1))) == 1 << k
