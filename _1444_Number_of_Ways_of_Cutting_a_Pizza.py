from functools import lru_cache


class Solution:
    def ways(self, pizza, k):
        ## Approach 2, conciser
        @lru_cache(None)
        def dfs(i, j, k):
            if A[m][n] - A[m][j] - A[i][n] + A[i][j] == 0: return 0
            if k == 1: return 1
            ans = 0
            for r in range(i, m-1):
                if A[r+1][n] - A[i][n] - A[r+1][j] + A[i][j] == 0: continue
                ans += dfs(r+1, j, k-1)
            for c in range(j, n-1):
                if A[m][c+1] - A[m][j] - A[i][c+1] + A[i][j] == 0: continue
                ans += dfs(i, c+1, k-1)
            return ans % (10**9 + 7)
        
        m, n = len(pizza), len(pizza[0])
        A = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                A[i][j] = (pizza[i-1][j-1] == 'A') + A[i-1][j] + A[i][j-1] - A[i-1][j-1]
        return dfs(0, 0, k)
        
        ## Approach 1
        # @lru_cache(None)
        # def dfs(i1, j1, i2, j2, k):
        #     if k == 1:
        #         if A[i2+1][j2+1] - A[i2+1][j1] - A[i1][j2+1] + A[i1][j1] == 0: return 0
        #         else: return 1
        #     ans = 0
        #     for i in range(i1, i2):
        #         ans += dfs(i1, j1, i, j2, 1) * dfs(i+1, j1, i2, j2, k-1)
        #     for j in range(j1, j2):
        #         ans += dfs(i1, j1, i2, j, 1) * dfs(i1, j+1, i2, j2, k-1)
        #     return ans
        # m, n = len(pizza), len(pizza[0])
        # A = [[0] * (n+1) for _ in range(m+1)]
        # for i in range(1, m+1):
        #     for j in range(1, n+1):
        #         A[i][j] = (pizza[i-1][j-1] == 'A') + A[i-1][j] + A[i][j-1] - A[i-1][j-1]
        # return dfs(0, 0, m-1, n-1, k) % (10**9 + 7)
