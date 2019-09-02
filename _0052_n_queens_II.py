class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        backtracking again. :-)
        diagonal check:
            1. col - row with last col - row
            2. col + row with last col + row
        time : O(n^n)
        space: O(n)
        """
        self.res = 0
        cols, d1, d2 = [False] * n, [False] * n * 2, [False] * n * 2
        self.helper(0, cols, d1, d2, n)
        return self.res

    def helper(self, row, cols, d1, d2, n):
        if row == n:
            self.res += 1
            return
        for col in xrange(n):
            id1 = col - row + n
            id2 = col + row
            if cols[col] or d1[id1] or d2[id2]: continue
            cols[col] = d1[id1] = d2[id2] = True
            self.helper(row + 1, cols, d1, d2, n)
            cols[col] = d1[id1] = d2[id2] = False