class Solution(object):
    def longestAwesome(self, s):
        """
        :type s: str
        :rtype: int
        """
        mask = 0
        d = {0: -1}
        res = 0
        for i, x in enumerate(s):
            mask ^= 1 << int(x)
            if mask not in d: d[mask] = i
            else: res = max(res, i-d[mask])
            for j in xrange(10):
                odd_pair = mask ^ 1 << j
                if odd_pair in d: res = max(res, i-d[odd_pair])
        return res
