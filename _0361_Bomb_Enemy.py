class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ## Approach 4
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        up, down  = [[0] * (n+1) for _ in xrange(m+1)], [[0] * (n+1) for _ in xrange(m+1)]
        left, right = [[0] * (n+1) for _ in xrange(m+1)], [[0] * (n+1) for _ in xrange(m+1)]
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if grid[i-1][j-1] == 'E':
                    up[i][j] = up[i-1][j] + 1
                    left[i][j] = left[i][j-1] + 1
                elif grid[i-1][j-1] == '0':
                    up[i][j] = up[i-1][j]
                    left[i][j] = left[i][j-1]
        for i in xrange(m-1, -1, -1):
            for j in xrange(n-1, -1, -1):
                if grid[i][j] == 'E':
                    down[i][j] = down[i+1][j] + 1
                    right[i][j] = right[i][j+1] + 1
                elif grid[i][j] == '0':
                    down[i][j] = down[i+1][j]
                    right[i][j] = right[i][j+1]
        res = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '0':
                    res = max(res, up[i+1][j+1]+left[i+1][j+1]+down[i][j]+right[i][j])
        return res
        
        ## Approach 3
        # if not grid or not grid[0]: return 0
        # m, n = len(grid), len(grid[0])
        # def dfs(ii, jj, di, dj):
        #     if (ii, jj, di, dj) in cache: return cache[ii, jj, di, dj]
        #     i, j = ii, jj
        #     ans = 0
        #     while 0 <= i + di < m and 0 <= j + dj < n and grid[i + di][j + dj] != 'W':
        #         i += di
        #         j += dj
        #         if (i, j, di, dj) in cache:
        #             ans += cache[i, j, di, dj]
        #             cache[ii, jj, di, dj] = ans
        #             return ans
        #         if grid[i][j] == 'E':
        #             ans += 1
        #     cache[ii, jj, di, dj] = ans
        #     return ans
        # res = 0
        # dirs = [-1, 0, 1, 0, -1]
        # cache = dict()
        # for i in xrange(m):
        #     for j in xrange(n):
        #         if grid[i][j] == '0':
        #             cur = 0
        #             for k in xrange(4):
        #                 cur += dfs(i, j, dirs[k], dirs[k+1])
        #             res = max(res, cur)
        # return res 
                
        ## Approach 2
        # if not grid or not grid[0]: return 0
        # m, n = len(grid), len(grid[0])
        # dp = [[[0, 0] for _ in xrange(n+2)] for _ in xrange(m+2)]
        # for i in xrange(1, m+1):
        #     for j in xrange(1, n+1):
        #         if grid[i-1][j-1] == 'E':
        #             dp[i][j][1] = dp[i][j-1][1] + 1
        #             dp[i][j][0] = dp[i-1][j][0] + 1
        #         elif grid[i-1][j-1] == '0':
        #             dp[i][j][1] = dp[i][j-1][1]
        #             dp[i][j][0] = dp[i-1][j][0]
        # res = 0
        # for i in xrange(m, 0, -1):
        #     for j in xrange(n, 0, -1):
        #         if grid[i-1][j-1] == 'E':
        #             dp[i][j][1] = dp[i][j+1][1] + 1
        #             dp[i][j][0] = dp[i+1][j][0] + 1
        #         elif grid[i-1][j-1] == '0':
        #             res = max(res, sum(dp[i][j]) + dp[i][j+1][1] + dp[i+1][j][0])
        #             dp[i][j][1] = dp[i][j+1][1]
        #             dp[i][j][0] = dp[i+1][j][0]
        # return res

        ## Approach 1
        # if not grid or not grid[0]: return 0
        # m, n = len(grid), len(grid[0])
        # def helper(ii, jj):
        #     ans = 0
        #     i = ii
        #     while i >= 0 and grid[i][jj] != 'W':
        #         if grid[i][jj] == 'E': ans += 1
        #         i -= 1
        #     i = ii
        #     while i < m and grid[i][jj] != 'W':
        #         if grid[i][jj] == 'E': ans += 1
        #         i += 1
        #     j = jj
        #     while j >= 0 and grid[ii][j] != 'W':
        #         if grid[ii][j] == 'E': ans += 1
        #         j -= 1
        #     j = jj
        #     while j < n and grid[ii][j] != 'W':
        #         if grid[ii][j] == 'E': ans += 1
        #         j += 1
        #     return ans
        # res = 0
        # for i in xrange(m):
        #     for j in xrange(n):
        #         if grid[i][j] == '0':
        #             res = max(res, helper(i, j))
        # return res
