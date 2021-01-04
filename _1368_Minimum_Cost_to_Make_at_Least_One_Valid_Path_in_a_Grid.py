from collections import deque


class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
            variant of dijkstra algorithm
        """
        dq = deque([[0, 0, 0]])
        res = float('inf')
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m, n = len(grid), len(grid[0])
        seen = set()
        while dq:
            i, j, d = dq.popleft()
            if (i, j) in seen: continue
            seen.add((i, j))
            if i < 0 or i == m or j < 0 or j == n: continue
            if i == m-1 and j == n-1: res = min(res, d)
            for k, (di, dj) in enumerate(dirs, 1):
                ni, nj = i + di, j + dj
                if k == grid[i][j]:
                    dq.appendleft([ni, nj, d])
                else:
                    dq.append([ni, nj, d+1])
        return res
