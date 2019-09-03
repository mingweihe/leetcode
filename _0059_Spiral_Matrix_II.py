class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0]*n for _ in xrange(n)]
        row_begin = col_begin = 0
        row_end = col_end = n - 1
        num = 1
        while row_begin <= row_end and col_begin <= col_end:
            for i in xrange(col_begin, col_end+1):
                matrix[row_begin][i] = num
                num += 1
            row_begin += 1
            print matrix
            for i in xrange(row_begin, row_end+1):
                matrix[i][col_end] = num
                num += 1
            col_end -= 1
            for i in xrange(col_end, col_begin-1, -1):
                matrix[row_end][i] = num
                num += 1
            row_end -= 1
            for i in xrange(row_end, row_begin-1, -1):
                matrix[i][col_begin] = num
                num += 1
            col_begin += 1
        return matrix
