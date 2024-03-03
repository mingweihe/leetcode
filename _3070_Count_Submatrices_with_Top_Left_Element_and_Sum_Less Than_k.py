class Solution(object):
    def countSubmatrices(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        cnt = 0
        m, n = len(grid), len(grid[0])
        A = [[0]*(n+1) for _ in xrange(m+1)]
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                A[i][j] = A[i-1][j] + A[i][j-1] - A[i-1][j-1] + grid[i-1][j-1]
                cnt += A[i][j] <= k
        return cnt
