from heapq import heappop, heappush

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        hq = []
        m, n = len(heightMap), len(heightMap[0])
        seen = set()
        for i in xrange(m):
            for j in xrange(n):
                if i in (0, m-1) or j in (0, n-1):
                    heappush(hq, [heightMap[i][j], i, j])
                    seen.add((i, j))
        res = 0
        cur_max = float('-inf')
        dirs = [-1, 0, 1, 0, -1]
        while hq:
            h, i, j = heappop(hq)
            cur_max = max(cur_max, h)
            for k in xrange(4):
                n_i, n_j = i + dirs[k], j + dirs[k+1]
                if not (0 <= n_i < m and 0 <= n_j < n): continue
                if (n_i, n_j) in seen: continue
                seen.add((n_i, n_j))
                cur_h = heightMap[n_i][n_j]
                heappush(hq, [cur_h, n_i, n_j])
                res += max(0, cur_max - cur_h)
        return res
