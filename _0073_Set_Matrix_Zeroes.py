class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix: return
        n, m = len(matrix), len(matrix[0])
        row_0, col_0 = False, False
        for i in xrange(n):
            for j in xrange(m):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
                    if i == 0: row_0 = True
                    if j == 0: col_0 = True
        for i in xrange(1, n):
            for j in xrange(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if row_0:
            for i in xrange(m):
                matrix[0][i] = 0
        if col_0:
            for i in xrange(n):
                matrix[i][0] = 0
