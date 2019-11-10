import collections


class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        dirs = [[0,-1],[0,1],[1,0],[-1,0]]
        m, n = len(grid), len(grid[0])
        queue = collections.deque()
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 0:
                    queue.append([i, j])
                    closed = 1
                    while queue:
                        x, y = queue.popleft()
                        grid[x][y] = 1
                        if x in (0, m - 1) or y in (0, n - 1): closed = 0
                        for a, b in dirs:
                            x1, y1 = x+a, y+b
                            if -1 < x1 < m and -1 < y1 < n and grid[x1][y1] == 0:
                                queue.append([x1, y1])
                    res += closed
        return res
