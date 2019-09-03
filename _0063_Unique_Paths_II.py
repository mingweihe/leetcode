class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        dp = [0]*m  # length of dp should equal width of grid
        dp[0] = 1
        for i in xrange(n):
            for j in xrange(m):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:  # j > 0 first dp element will be taken are by first case
                    dp[j] += dp[j-1]
        return dp[-1]