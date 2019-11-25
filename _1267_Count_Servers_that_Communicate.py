import collections


class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = set()
        m, n = len(grid), len(grid[0])
        H = collections.defaultdict(set)
        V = collections.defaultdict(set)
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    H[i].add((i, j))
                    V[j].add((i, j))
        for X in (H, V):
            for k, sets in X.items():
                if len(sets) > 1:
                    for co in sets:
                        res.add(co)
        return len(res)
