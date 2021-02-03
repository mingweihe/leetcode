class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        res = 0
        for i in xrange(m):
            for j in xrange(n):
                if i == j or i + j == m - 1:
                    res += mat[i][j]
        return res
