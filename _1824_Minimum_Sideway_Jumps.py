class Solution(object):
    def minSideJumps(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: int
        """
        n = len(obstacles)
        dp = [[float('inf')] * 3 for _ in xrange(n)]
        dp[0] = [1, 0, 1]
        for i in xrange(1, n):
            for j in xrange(3):
                if obstacles[i] - 1 == j: continue
                dp[i][j] = dp[i-1][j]
            for j in xrange(3):
                if obstacles[i] - 1 == j: continue
                dp[i][j] = min(dp[i][j], dp[i][(j+1)%3] + 1)
                dp[i][j] = min(dp[i][j], dp[i][(j+2)%3] + 1)
        return min(dp[-1])
