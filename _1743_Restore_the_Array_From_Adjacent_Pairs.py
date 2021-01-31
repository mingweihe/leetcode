from collections import defaultdict


class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        nexts = defaultdict(list)
        start_end = set()
        for u, v in adjacentPairs:
            if u in start_end: start_end.discard(u)
            else: start_end.add(u)
            if v in start_end: start_end.discard(v)
            else: start_end.add(v)
            nexts[u] += v,
            nexts[v] += u,
        start = start_end.pop()
        res = [start]
        for _ in xrange(len(adjacentPairs)):
            arr = nexts[res[-1]]
            if len(arr) == 1: res += arr[0],
            else: res += res[-2] ^ arr[0] ^ arr[1],
        return res
