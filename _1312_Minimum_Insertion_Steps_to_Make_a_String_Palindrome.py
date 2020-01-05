# python 3 only
from functools import lru_cache


class Solution:
    def minInsertions(self, s):

        @lru_cache(None)
        def dp(i, j):
            if i > j: return float('inf')
            if i == j: return 0
            if i == j - 1: return +(s[i] != s[j])
            if s[i] == s[j]: return dp(i + 1, j - 1)
            return min(dp(i + 1, j), dp(i, j - 1)) + 1

        return dp(0, len(s) - 1)
