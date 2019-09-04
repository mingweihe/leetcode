from collections import deque


class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        BFS
        """
        N = len(grid)
        q = deque([(i, j) for i in xrange(N) for j in xrange(N) if grid[i][j] == 1])
        if len(q) in (N*N, 0): return -1
        res = -1
        dirs = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        while q:
            for _ in xrange(len(q)):
                x, y = q.popleft()
                for i, j in dirs:
                    xi, yj = x+i, y+j
                    if -1 < xi < N and -1 < yj < N and grid[xi][yj] == 0:
                        q.append((xi, yj))
                        grid[xi][yj] = 1
            res += 1
        return res
