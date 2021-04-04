from collections import defaultdict


class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        d = defaultdict(set)
        for a, b in logs:
            d[a].add(b)
        cnt = defaultdict(int)
        for _, v in d.items():
            cnt[len(v)] += 1
        return [cnt[i] for i in xrange(1, k+1)]
