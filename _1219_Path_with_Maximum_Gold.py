class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(x, y, visited):
            if (x, y) in visited: return 0
            if x < 0 or x == m or y < 0 or y == n: return 0
            if grid[x][y] == 0: return 0
            ans = grid[x][y]
            visited.add((x, y))
            cur = 0
            for a, b in dirs:
                x1, y1 = x+a, y+b
                cur = max(cur, dfs(x1, y1, visited))
            visited.discard((x, y))
            return ans + cur
        res = 0
        m, n = len(grid), len(grid[0])
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] != 0:
                    res = max(res, dfs(i, j, set()))
        return res
