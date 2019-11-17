class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        n, m = len(grid), len(grid[0])
        for i in xrange(k):
            x = grid[n-1][m-1]
            for j in xrange(n-1, 0, -1):
                grid[j][m-1] = grid[j-1][m-1]
            grid[0][m-1] = x
            for j in xrange(n):
                x = grid[j][m-1]
                for k in xrange(m-1, 0, -1):
                    grid[j][k] = grid[j][k-1]
                grid[j][0] = x
        return grid
