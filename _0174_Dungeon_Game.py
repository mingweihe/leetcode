class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        M, N = len(dungeon), len(dungeon[0])
        dp = [1]*(N+1)
        for i in xrange(M-1, -1 , -1):
            for j in xrange(N-1, -1, -1):
                if j == N-1: dp[j] = max(1, dp[j]-dungeon[i][j])
                elif i == M-1: dp[j] = max(1, dp[j+1]-dungeon[i][j])
                else: dp[j] = max(1, min(dp[j]-dungeon[i][j], dp[j+1]-dungeon[i][j]))
        return dp[0]
