from collections import defaultdict


class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        ss = defaultdict(set)
        ss[0].add(0)
        for p in stones:
            for k in ss[p]:
                for nk in (k-1, k, k+1):
                    if nk > 0:
                        ss[p+nk].add(nk)
        return ss[stones[-1]]
