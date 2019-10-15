class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        def dfs(i, j, d1, d2):
            if 0 <= i < 8 and 0 <= j < 8:
                if board[i][j]:
                    res.append([i, j])
                    return
                dfs(i+d1, j+d2, d1, d2)
        res = []
        board = [[0] * 8 for _ in xrange(8)]
        for x, y in queens:
            board[x][y] = 1
        dirs = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]
        for di in dirs:
            dfs(king[0], king[1], di[0], di[1])
        return res
