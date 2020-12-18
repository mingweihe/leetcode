from functools import lru_cache
from itertools import combinations


class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        d = len(nums) // k
        @lru_cache(None)
        def dfs(nums):
            if not nums: return 0
            ans = float('inf')
            for A in combinations(set(nums), d):
                left = list(nums)
                for x in A:
                    left.remove(x)
                ans = min(ans, max(A)-min(A)+dfs(tuple(left)))
            return ans
        res = dfs(tuple(nums))
        return -1 if res == float('inf') else res
