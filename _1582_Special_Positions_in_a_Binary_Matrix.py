class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        rows, cols = [0] * m, [0] * n
        for i in xrange(m):
            for j in xrange(n):
                rows[i] += mat[i][j]
                cols[j] += mat[i][j]
        res = 0
        for i in xrange(m):
            for j in xrange(n):
                res += mat[i][j] == rows[i] == cols[j] == 1
        return res
