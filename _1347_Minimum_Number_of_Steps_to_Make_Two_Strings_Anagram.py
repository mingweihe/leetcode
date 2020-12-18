import collections


class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        cnt = collections.Counter(s)
        for c in t:
            if cnt[c] > 0: cnt[c] -= 1
        return sum(cnt.values())
