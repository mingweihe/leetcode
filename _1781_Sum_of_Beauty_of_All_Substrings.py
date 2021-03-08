from collections import defaultdict


class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, n = 0, len(s)
        for i in xrange(n):
            d = defaultdict(int)
            for j in xrange(i, n):
                d[s[j]] += 1
                maxi, mini = float('-inf'), float('inf')
                for x in d.values():
                    maxi = max(maxi, x)
                    mini = min(mini, x)
                res += maxi-mini
        return res
