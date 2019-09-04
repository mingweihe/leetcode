class Solution(object):
    def lastSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        i, L = 0, len(s)
        res = ''
        while i < L:
            res = max(res, s[i:])
            while i < L - 1 and s[i] == s[i+1]:
                i += 1
            i += 1
        return res
