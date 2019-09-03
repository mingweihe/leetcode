class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self._exist(board, i, j, word, 0):
                    return True
        return False

    def _exist(self, board, i, j, word, start):
        if start == len(word): return True
        if i < 0 or i == len(board) or j < 0 or j == len(board[0]): return False
        c = board[i][j]
        if c == word[start]:
            start += 1
            board[i][j] = '#'
            res = self._exist(board, i, j + 1, word, start) \
                  or self._exist(board, i, j - 1, word, start) \
                  or self._exist(board, i + 1, j, word, start) \
                  or self._exist(board, i - 1, j, word, start)
            board[i][j] = c
            return res
        return False
