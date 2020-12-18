class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = -1
        for i in xrange(len(s)/2):
            for j in xrange(len(s)-1, i, -1):
                if s[i] == s[j]:
                    res = max(res, j - i - 1)
        return res
