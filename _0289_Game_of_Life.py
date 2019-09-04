class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if board is None or len(board) == 0: return
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                cnt = self.countLive(board, i, j)
                if board[i][j] == 1:
                    if cnt in (2, 3):
                        board[i][j] = 3  # board[i][j] += 2 -> bit 10
                elif cnt == 3:
                    board[i][j] = 2  # board[i][j] += 2 -> bit 10
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                board[i][j] >>= 1

    def countLive(self, board, i, j):
        cnt = 0
        top, bottom = max(0, i - 1), min(len(board) - 1, i + 1)
        left, right = max(0, j - 1), min(len(board[0]) - 1, j + 1)
        for x in xrange(top, bottom + 1):
            for y in xrange(left, right + 1):
                if x == i and y == j: continue
                cnt += board[x][y] & 1  # last bit digit
        return cnt
