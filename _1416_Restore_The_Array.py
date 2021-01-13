class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        ## Approach 2, bottom-up dp, O(n*log10(k))
        MOD = 10 ** 9 + 7
        n = len(s)
        dp = [0] * n + [1]
        for i in range(n-1, -1, -1):
            num = 0
            if s[i] == '0': continue
            for j in range(i, n):
                num = num * 10 + int(s[j])
                if num > k: break
                dp[i] = (dp[i] + dp[j+1]) % MOD
        return dp[0]
        
        ## Approach 1, top-down dp, O(n*log10(k))
        # MOD = 10**9 + 7
        # @lru_cache(None)
        # def dp(i):
        #     if i == len(s): return 1
        #     if s[i] == '0': return 0
        #     num, res = 0, 0
        #     for j in range(i, len(s)):
        #         num = num * 10 + int(s[j])
        #         if num > k: break
        #         res = (res + dp(j+1)) % MOD
        #     return res
        # return dp(0)
