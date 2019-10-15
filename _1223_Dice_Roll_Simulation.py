class Solution(object):
    def dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        # Approach 2 2D dynamic programming
        M = 10 ** 9 + 7
        dp = [[0, 1] + [0] * 15 for _ in xrange(6)]
        for _ in xrange(n - 1):
            dp2 = [[0] * 17 for _ in xrange(6)]
            for i in xrange(6):
                for k in xrange(1, rollMax[i] + 1):
                    for j in xrange(6):
                        if i == j:
                            if k < rollMax[i]:
                                dp2[j][k + 1] += dp[i][k] % M
                        else:
                            dp2[j][1] += dp[i][k] % M
            dp = dp2
        return sum(map(sum, dp)) % M

        # Approach 1 memorized recursion
        # M = 10**9 + 7
        # cache = dict()
        # def dfs(i, j, k):
        #     if (i, j, k) in cache:
        #         return cache[i, j, k]
        #     if i == 0: return 1
        #     res = 0
        #     for d in xrange(6):
        #         if d != j:
        #             res += dfs(i-1, d, 1)
        #         elif k < rollMax[d]:
        #             res += dfs(i-1, d, k+1)
        #     res %= M
        #     cache[i, j, k] = res
        #     return res
        # return dfs(n, 0, 0) % M
