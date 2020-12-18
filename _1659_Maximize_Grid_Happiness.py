from functools import lru_cache


class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        def get_happiness(pos, prev, choice):
            up, left = prev[0], prev[-1]
            if pos / m == 0: up = 0
            if pos % n == 0: left = 0
            up_offset = -30 if up == 1 else 20 if up == 2 else 0
            left_offset = -30 if left == 1 else 20 if left == 2 else 0
            neighbors = bool(up) + bool(left)
            ans = 0
            if choice == 1:
                ans = 120 + up_offset + left_offset - 30 * neighbors
            elif choice == 2:
                ans = 40 + up_offset + left_offset + 20 * neighbors
            return ans
        
        @lru_cache(None)
        def dfs(pos, ic, ec, prev):
            if pos == m*n: return 0
            ans = dfs(pos+1, ic, ec, prev[1:] + (0,))
            if ic:
                gained_i = get_happiness(pos, prev, 1)
                ans = max(ans, gained_i + dfs(pos+1, ic-1, ec, prev[1:] + (1,)))
            if ec:
                gained_e = get_happiness(pos, prev, 2)
                ans = max(ans, gained_e + dfs(pos+1, ic, ec-1, prev[1:] + (2,)))
            return ans
        return dfs(0, introvertsCount, extrovertsCount, tuple([0]*n))
