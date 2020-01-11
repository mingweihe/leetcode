class Solution(object):
    def matrixBlockSum(self, mat, K):
        """
        :type mat: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        L, W = min(m, m+K+1), min(n, n+K+1)
        res = [[0] * W for _ in xrange(L)]
        dp = [[0]*(n+1) for _ in xrange(m+1)]
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                dp[i][j] = mat[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

        for i in xrange(L):
            for j in xrange(W):
                r_min, r_max = max(i-K, 0), min(m-1, i+K)
                c_min, c_max = max(j-K, 0), min(n-1, j+K)
                res[i][j] = dp[r_max+1][c_max+1] - dp[r_max+1][c_min] - dp[r_min][c_max+1] + dp[r_min][c_min]
        return res
