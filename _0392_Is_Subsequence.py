class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i, j = 0, 0
        L1, L2 = len(s), len(t)
        while i < L1 and j < L2:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == L1
