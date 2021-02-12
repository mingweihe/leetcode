from collections import defaultdict


class Solution(object):
    def canConvertString(self, s, t, k):
        """
        :type s: str
        :type t: str
        :type k: int
        :rtype: bool
        """
        if len(s) != len(t): return False
        d = defaultdict(int)
        for i in xrange(len(s)):
            shift = ord(t[i]) - ord(s[i])
            if shift == 0: continue
            if shift < 0: shift += 26
            d[shift] += 1
            
        for shift, times in d.items():
            if (times-1) * 26 + shift > k: return False
        return True
