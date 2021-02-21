class Solution:
    def maximumScore(self, nums, multipliers):
        ## Approach 2, bottom-up DP
        n, m = len(nums), len(multipliers)
        # pick i numbers from the left, pick j numbers from the right
        dp = [[0] * (m+1) for _ in range(m+1)]
        for k in range(1, m+1):
            for l in range(k+1):
                l_pick = float('-inf') if l == 0 else multipliers[k-1] * nums[l-1] + dp[l-1][k-l]
                r_pick = float('-inf') if l == k else multipliers[k-1] * nums[n-(k-l)] + dp[l][k-l-1]
                dp[l][k-l] = max(l_pick, r_pick)
        return max(dp[l][m-l] for l in range(m+1))
        
        ## Approach 1, top-down DP with tricky number
        # @lru_cache(2000)
        # def dfs(i, j):
        #     k = n-(j-i+1)
        #     if k == m: return 0
        #     ans1 = multipliers[k] * nums[i] + dfs(i+1, j)
        #     ans2 = multipliers[k] * nums[j] + dfs(i, j-1)
        #     return max(ans1, ans2)
        # n, m = len(nums), len(multipliers)
        # return dfs(0, len(nums)-1)
