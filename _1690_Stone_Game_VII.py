class Solution(object):
    def stoneGameVII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # Approach 2 bottom-up, less memory & faster running time
        accums = [0]
        for x in stones:
            accums += accums[-1] + x,
        n = len(stones)
        dp = [[0] * n for _ in xrange(n)]
        for l in xrange(2, n+1):
            for i in xrange(0, n-l+1):
                j = i+l-1
                dp[i][j] = max(accums[j]-accums[i]-dp[i][j-1], accums[j+1]-accums[i+1]-dp[i+1][j])
        return dp[0][n-1]
        
        ## Approach 1 top-down
        # accums = [0]
        # for x in stones:
        #     accums += accums[-1] + x,
        # n = len(stones)
        # memo = [[0] * n for _ in xrange(n)]
        # def dfs(i, j):
        #     if i==j: return 0
        #     if memo[i][j] != 0: return memo[i][j]
        #     res = max(accums[j]-accums[i]-dfs(i, j-1), accums[j+1]-accums[i+1]-dfs(i+1, j))
        #     memo[i][j] = res
        #     return res
        # return dfs(0, n-1)
