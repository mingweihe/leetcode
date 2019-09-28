class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # Approach 3, maintaining values on the fly
        # time O(m*n) space O(m+n)
        if not M: return 0
        res, m, n = 0, len(M), len(M[0])
        cols = [0] * n
        diagonals, anti_diagonals = [0] * (m+n), [0] * (m+n)
        for i in xrange(m):
            row = 0
            for j in xrange(n):
                if M[i][j] == 1:
                    row += 1
                    cols[j] += 1
                    anti_diagonals[i+j] += 1
                    diagonals[j-i+m] += 1
                    res = max(res, row)
                    res = max(res, cols[j])
                    res = max(res, anti_diagonals[i+j])
                    res = max(res, diagonals[j-i+m])
                else:
                    row = 0
                    cols[j] = 0
                    anti_diagonals[i+j] = 0
                    diagonals[j-i+m] = 0
        return res

        # Approach 2, 3D dp
        # time O(m*n) space O(m*n*4)
        # if not M: return 0
        # dirs = [[0,-1], [-1, -1], [-1, 0], [-1,1]]
        # m, n, res = len(M), len(M[0]), 0
        # dp = [[[0]*4 for _ in xrange(n)] for _ in xrange(m)]
        # for i in xrange(m):
        #     for j in xrange(n):
        #         if M[i][j] == 0: continue
        #         k = 0
        #         for d1, d2 in dirs:
        #             x, y = i+d1, j+d2
        #             if x >= 0 and 0 <= y < n: dp[i][j][k] = dp[x][y][k] + 1
        #             else: dp[i][j][k] = 1
        #             res = max(res, dp[i][j][k])
        #             k += 1
        # return res

        # Approach 1, optimized dfs
        # time O(m*n*len(diagonal)) space O(1)
        # if not M: return 0
        # dirs = [[0,1], [1, 0], [1, 1], [-1,1]]
        # res = 0
        # L1, L2 = len(M), len(M[0])
        # def dfs(m, n, x, y):
        #     mr, nr = m-x, n-y
        #     if 0 <= mr < L1 and 0 <= nr < L2 and M[mr][nr] == 1: return 0
        #     ans = 1
        #     m1, n1 = m + x, n + y
        #     while 0 <= m1 < L1 and 0 <= n1 < L2 and M[m1][n1] == 1:
        #         ans += 1
        #         m1, n1 = m1 + x, n1 + y
        #     return ans
        # for i in xrange(L1):
        #     for j in xrange(L2):
        #         if M[i][j] == 1:
        #             for d1, d2 in dirs:
        #                 res = max(res, dfs(i, j, d1, d2))
        # return res
