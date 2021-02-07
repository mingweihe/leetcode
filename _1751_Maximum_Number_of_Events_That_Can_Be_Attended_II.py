from functools import lru_cache
from bisect import bisect_left


class Solution:
    def maxValue(self, events, k):
        # Approach 2, top-down DP
        @lru_cache(None)
        def dp(i, k):
            if i == n or k == 0: return 0
            ans = dp(i+1, k)
            next_i = bisect_left(events, [events[i][1]+1])
            ans = max(ans, events[i][2] + dp(next_i, k-1))
            return ans
        n = len(events)
        events.sort()
        return dp(0, k)
        
        # Approach 1, bottom up DP
        # n = len(events)
        # events.sort(key=lambda x: x[1])
        # dp, dp2 = [[0, 0]], [[0, 0]]
        # ans = float('-inf')
        # for _ in range(k):
        #     for s, e, v in events:
        #         i = bisect_right(dp, [s]) - 1
        #         if dp[i][1] + v > dp2[-1][1]:
        #             dp2 += [e, dp[i][1] + v],
        #     dp, dp2 = dp2, [[0, 0]]
        # return dp[-1][-1]
