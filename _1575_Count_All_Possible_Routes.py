from functools import lru_cache


class Solution:
    def countRoutes(self, locations, start, finish, fuel):
        @lru_cache(None)
        def dfs(cur_city, cur_fuel):
            if cur_fuel < 0: return 0
            ans = 0 if cur_city != finish else 1
            for i, loc in enumerate(locations):
                if i == cur_city: continue
                ans += dfs(i, cur_fuel - abs(locations[cur_city] - loc))
            return ans
        return dfs(start, fuel) % (10**9 + 7)
