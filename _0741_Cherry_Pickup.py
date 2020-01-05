class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Approach 2, Time O(n^3), Space O(n^2)
        N, M = len(grid), (len(grid) << 1) - 1
        dp = [[0] * N for _ in xrange(N)]
        dp[0][0] = grid[0][0]
        for n in xrange(1, M):
            for i in xrange(N - 1, -1, -1):
                j = n - i
                for p in xrange(N - 1, -1, -1):
                    q = n - p
                    if j < 0 or j >= N or grid[i][j] == -1 or q < 0 or q >= N or grid[p][q] == -1:
                        dp[i][p] = -1
                        continue
                    if i > 0: dp[i][p] = max(dp[i][p], dp[i - 1][p])
                    if p > 0: dp[i][p] = max(dp[i][p], dp[i][p - 1])
                    if i > 0 and p > 0: dp[i][p] = max(dp[i][p], dp[i - 1][p - 1])
                    if dp[i][p] >= 0:
                        dp[i][p] += grid[i][j] + (grid[p][q] if i != p else 0)
        return max(dp[-1][-1], 0)

        # Approach 1, Time O(n^3), Space O(n^3), but faster
        # N = len(grid)
        # dp = [[[-1]*(N+1) for _ in xrange(N+1)] for _ in xrange(N+1)]
        # dp[1][1][1] = grid[0][0]
        # for i in xrange(1, N+1):
        #     for j in xrange(1, N+1):
        #         if grid[i-1][j-1] == -1: continue
        #         for k in xrange(max((i+j-N), 1), min(i+j, N+1)):
        #             l = i+j-k
        #             if grid[k-1][l-1] == -1: continue
        #             last_best = max(dp[i-1][j][k], dp[i][j-1][k], dp[i-1][j][k-1], dp[i][j-1][k-1])
        #             if last_best == -1: continue
        #             last_best += grid[i-1][j-1] + (grid[k-1][l-1] if i != k else 0)
        #             dp[i][j][k] = max(dp[i][j][k], last_best)
        # return max(dp[-1][-1][-1], 0)
