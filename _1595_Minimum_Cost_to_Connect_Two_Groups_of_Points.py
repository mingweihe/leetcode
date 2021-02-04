class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(idx, mask):
            if idx == size1:
                ans = 0
                for i in range(size2):
                    if mask & 1 << i == 0:
                        ans += min_cost2[i]
                return ans
            ans = float('inf')
            for i in range(size2):
                ans = min(ans, dfs(idx + 1, mask | 1 << i) + cost[idx][i])
            return ans
        
        size1, size2 = len(cost), len(cost[0])
        min_cost2 = [float('inf')] * size2
        for i in range(size1):
            for j in range(size2):
                min_cost2[j] = min(min_cost2[j], cost[i][j])
        return dfs(0, 0)
