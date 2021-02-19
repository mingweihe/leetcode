from functools import lru_cache


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(r, c1, c2):
            if r == m: return 0
            if c1 < 0 or c2 < 0 or c1 == n or c2 == n: return float('-inf')
            chrries = grid[r][c1] if c1 == c2 else grid[r][c1] + grid[r][c2]
            ans = 0
            for nc1 in range(c1-1, c1+2):
                for nc2 in range(c2-1, c2+2):
                    ans = max(ans, chrries + dfs(r+1, nc1, nc2))
            return ans
        m, n = len(grid), len(grid[0])
        return dfs(0, 0, n-1)
