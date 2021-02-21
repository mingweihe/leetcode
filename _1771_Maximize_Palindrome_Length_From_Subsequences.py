from functools import lru_cache


class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if i > j: return 0
            if i == j: return 1
            ans = 0
            if W[i] == W[j]:
                ans = 2 + dfs(i+1, j-1)
                if i < m and j >= m and ans > self.res: self.res = ans
            else:
                ans = max(dfs(i+1, j), dfs(i, j-1))
            return ans
        W = word1 + word2
        m, n = len(word1), len(word2)
        self.res = float('-inf')
        dfs(0, len(W)-1)
        return 0 if self.res == float('-inf') else self.res
