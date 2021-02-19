from functools import lru_cache


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        ## Approach 1, top-down DP O(n^3)
        pres = [0] + list(accumulate(stoneValue))
        @lru_cache(None)
        def dfs(i, j):
            if i == j: return 0
            ans = 0
            for k in range(i, j):
                left = pres[k+1]-pres[i]
                right = pres[j+1]-pres[k+1]
                if left <= right: ans = max(ans, left + dfs(i, k))
                if right <= left: ans = max(ans, right + dfs(k+1, j))
            return ans
        return dfs(0, len(stoneValue)-1)
