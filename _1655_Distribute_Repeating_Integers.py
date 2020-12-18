from functools import lru_cache
from collections import Counter


class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        cnts = list(Counter(nums).values())
        m = len(quantity)
        n = len(cnts)
        sums = [0] * 2**m
        for i in range(2**m):
            for j in range(m):
                if i & 1 << j:
                    sums[i] += quantity[j]
        
        @lru_cache(None)
        def dp(mask, idx):
            if mask == 0: return True
            if idx < 0: return False
            cur = mask
            while cur:
                if sums[cur] <= cnts[idx] and dp(cur ^ mask, idx-1):
                    return True
                cur = (cur - 1) & mask
            return dp(mask, idx-1)
        
        return dp((1<<m)-1, n-1)
