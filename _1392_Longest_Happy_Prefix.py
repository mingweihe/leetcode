class Solution(object):
    def longestPrefix(self, s):
        """
        :type s: str
        :rtype: str
            KMP algorithm, time: O(n), space: O(m)
        """
        nex = [0, 0]
        j = 0
        for i in xrange(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = nex[j]
            if s[i] == s[j]:
                j += 1
            nex += j,
        return s[:nex[-1]]
