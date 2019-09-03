class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
            think smart, dfs from all edges
        """
        if not board or not board[0]: return
        m, n = len(board)-1, len(board[0])-1
        for i in xrange(m+1):
            self.dfs(board, i, 0)
            self.dfs(board, i, n)
        for i in xrange(n+1):
            self.dfs(board, 0, i)
            self.dfs(board, m, i)
        for i in xrange(m+1):
            for j in xrange(n+1):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '*':
                    board[i][j] = 'O'

    def dfs(self, board, i, j):
        if i < 0 or j < 0 or i == len(board) or j == len(board[0]) or board[i][j] != 'O':
            return
        board[i][j] = '*'
        self.dfs(board, i, j+1)
        self.dfs(board, i, j-1)
        self.dfs(board, i+1, j)
        self.dfs(board, i-1, j)
