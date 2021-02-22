from functools import lru_cache


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @lru_cache(None)
        def get_power(val):
            if val == 1: return 0
            if val & 1: return 1 + get_power(val * 3 + 1)
            return 1 + get_power(val // 2)

        res = sorted(range(lo, hi+1), key = lambda x: [get_power(x), x])
        return res[k-1]
