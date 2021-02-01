from functools import lru_cache


class Solution:
    def minDays(self, n):
        @lru_cache(None)
        def dfs(remain):
            if remain <= 1: return remain
            return min(remain % 2 + dfs(remain // 2), remain % 3 + dfs(remain // 3)) + 1
        return dfs(n)
    
        # @lru_cache(None) TLE
        # def dfs(cnt):
        #     if cnt > n: return float('inf')
        #     if cnt == n: return 0
        #     return min(dfs(cnt+1), dfs(cnt*2), dfs(cnt*3)) + 1
        # return dfs(1) + 1
