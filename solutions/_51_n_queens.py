class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        if n == 0: return res
        self.helper(res, [0] * n, 0)
        return res

    def helper(self, res, queens, pos):
        if pos == len(queens):
            self.add_solution(res, queens)
            return
        for i in xrange(len(queens)):
            queens[pos] = i
            if self.is_valid(queens, pos):
                self.helper(res, queens, pos + 1)

    def add_solution(self, res, queens):
        one_solution = []
        for i in xrange(len(queens)):
            line = ''
            for j in xrange(len(queens)):
                if queens[i] == j:
                    line += 'Q'
                else:
                    line += '.'
            one_solution.append(line)
        res.append(one_solution)

    def is_valid(self, queens, pos):
        for i in xrange(0, pos):
            if queens[i] == queens[pos]:
                return False
            if abs(queens[i] - queens[pos]) == pos - i:
                return False
        return True
