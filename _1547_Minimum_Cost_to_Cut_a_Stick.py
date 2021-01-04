from functools import lru_cache


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        @lru_cache(None)
        def dp(i, j):
            ans = float('inf')
            for k in cuts:
                if i < k < j:
                    ans = min(ans, dp(i, k) + dp(k, j) + j - i)
            if ans == float('inf'): return 0
            return ans
        return dp(0, n)
