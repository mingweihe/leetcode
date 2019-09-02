class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
            1. double pointer
            2. flexibly using set / dict
        """
        res, sets, L = 0, set(), len(s)
        j = i = 0
        while i < L:
            if s[i] in sets:
                sets.discard(s[j])
                j += 1
            else:
                sets.add(s[i])
                i += 1
                res = max(res, i-j)
        return res
