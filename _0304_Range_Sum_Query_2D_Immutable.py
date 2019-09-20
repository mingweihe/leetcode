class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """

        m, n = len(matrix), 0 if not matrix else len(matrix[0])
        sums = self.sums = [[0] * (n + 1) for _ in xrange(m + 1)]
        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                sums[i][j] = sums[i][j - 1] + sums[i - 1][j] - sums[i - 1][j - 1] + matrix[i - 1][j - 1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sums = self.sums
        return sums[row2 + 1][col2 + 1] - sums[row2 + 1][col1] - sums[row1][col2 + 1] + sums[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
