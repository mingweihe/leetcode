class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        dp = [[[0] * n for _ in xrange(n)] for _ in xrange(m+1)]
        for k in xrange(1, m+1):
            for i in xrange(n):
                for j in xrange(i, n):
                    if mat[k-1][j] == 0: break
                    dp[k][i][j] = dp[k-1][i][j] + 1
        return sum([sum(map(sum, x)) for x in dp])
