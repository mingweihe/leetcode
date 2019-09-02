class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Method 3
        checker = set()
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] == '.': continue
                x = '{}[{}]'.format(i, board[i][j])
                y = '[{}]{}'.format(board[i][j], j)
                z = '{}[{}]{}'.format(i / 3, board[i][j], j / 3)
                if x in checker or y in checker or z in checker: return False
                checker.add(x)
                checker.add(y)
                checker.add(z)
        return True

        # Method 2
        # def valid(i, j):
        #     for k in xrange(9):
        #         if k == j: continue
        #         if board[i][k] == board[i][j]: return False
        #     for k in xrange(9):
        #         if k == i: continue
        #         if board[k][j] == board[i][j]: return False
        #     for x in xrange(i/3*3, i/3*3+3):
        #         for y in xrange(j/3*3, j/3*3+3):
        #             if x == i and y == j: continue
        #             if board[x][y] == board[i][j]: return False
        #     return True
        # for m in xrange(9):
        #     for n in xrange(9):
        #         if board[m][n] == '.': continue
        #         if not valid(m, n):
        #             return False
        # return True

        # Method 1
        # for i in xrange(9):
        #     row, col, square = set(), set(), set()
        #     for j in xrange(9):
        #         if board[i][j] != '.':
        #             if board[i][j] not in row:
        #                 row.add(board[i][j])
        #             else: return False
        #         if board[j][i] != '.':
        #             if board[j][i] not in col:
        #                 col.add(board[j][i])
        #             else: return False
        #         rowIndex = i / 3 * 3 # 000333666
        #         colIndex = i % 3 * 3 # 036036036
        #         cur = board[rowIndex + j / 3][colIndex + j % 3]
        #         if cur != '.':
        #             if cur not in square:
        #                 square.add(cur)
        #             else: return False
        # return True
