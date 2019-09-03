class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if i == 0 and j != 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0 and i != 0:
                    grid[i][j] += grid[i-1][j]
                elif i != 0 and j != 0:
                    grid[i][j] += min(grid[i][j-1], grid[i-1][j])
        return grid[-1][-1]
