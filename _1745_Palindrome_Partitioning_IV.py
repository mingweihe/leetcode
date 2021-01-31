class Solution:
    def checkPartitioning(self, s):
        # Approach 3, O(n^2), bootom up dp
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for j in range(n):
            for i in range(j+1):
                dp[i][j] = s[i] == s[j] and (i+1 >= j-1 or dp[i+1][j-1])
        for i in range(n-2):
            for j in range(i+1, n-1):
                if dp[0][i] and dp[i+1][j] and dp[j+1][n-1]:
                    return True
        return False
        
        ## Approach 2, O(n^2), bottom up dp
        # n = len(s)
        # dp = [[False] * n for _ in range(n)]
        # for L in range(1, n+1):
        #     for i in range(n-L+1):
        #         j = i + L - 1
        #         dp[i][j] = s[i] == s[j] and (i+1 >= j-1 or dp[i+1][j-1])
        # for i in range(n-2):
        #     for j in range(i+1, n-1):
        #         if dp[0][i] and dp[i+1][j] and dp[j+1][n-1]:
        #             return True
        # return False
        
        ## top down dp O(n^2)
#         @lru_cache(None)
#         def dfs(i, j):
#             if i >= j: return True
#             return s[i] == s[j] and dfs(i+1, j-1)

#         for i in range(len(s)-2):
#             for j in range(i+1, len(s)-1):
#                 if dfs(0, i) and dfs(i+1, j) and dfs(j+1, len(s)-1):
#                     return True
#         return False
