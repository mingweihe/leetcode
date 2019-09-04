class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res, n, m = 0, len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    if i == 0 or grid[i - 1][j] == 0: res += 2
                    if j == 0 or grid[i][j - 1] == 0: res += 2
        return res
