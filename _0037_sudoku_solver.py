class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        easy solution: backtracking/dfs to solve this puzzle
        better solutioin: refer to python3 code
        """
        # Approach 1
        def solve():
            for i in xrange(9):
                for j in xrange(9):
                    if board[i][j] == '.':
                        for k in xrange(1, 10):
                            filled_c = str(k)
                            if self.isValid(board, i, j, filled_c):
                                board[i][j] = filled_c
                                if solve(): return True
                                board[i][j] = '.'
                        return False
            return True

        solve()

    def isValid(self, board, i, j, filled_c):
        for k in xrange(9):
            if board[i][k] == filled_c: return False
            if board[k][j] == filled_c: return False
            if board[i / 3 * 3 + k / 3][j / 3 * 3 + k % 3] == filled_c: return False
        return True
    # Approach 2, super fast
    # def solveSudoku(self, board: List[List[str]]) -> None:
    #     """
    #     Do not return anything, modify board in-place instead.
    #     """
    #     self.board = board
    #     self.val = self.PossibleVals()
    #     self.Solver()
    #
    # def PossibleVals(self):
    #     a = "123456789"
    #     d, val = {}, {}
    #     for i in range(9):
    #         for j in range(9):
    #             ele = self.board[i][j]
    #             if ele != ".":
    #                 d[("r", i)] = d.get(("r", i), []) + [ele]
    #                 d[("c", j)] = d.get(("c", j), []) + [ele]
    #                 d[(i // 3, j // 3)] = d.get((i // 3, j // 3), []) + [ele]
    #             else:
    #                 val[(i, j)] = []
    #     for (i, j) in val.keys():
    #         inval = d.get(("r", i), []) + d.get(("c", j), []) + d.get((i // 3, j // 3), [])
    #         val[(i, j)] = [n for n in a if n not in inval]
    #     return val
    #
    # def Solver(self):
    #     if len(self.val) == 0:
    #         return True
    #     kee = min(self.val.keys(), key=lambda x: len(self.val[x]))
    #     nums = self.val[kee]
    #     for n in nums:
    #         update = {kee: self.val[kee]}
    #         if self.ValidOne(n, kee, update):  # valid choice
    #             if self.Solver():  # keep solving
    #                 return True
    #         self.undo(kee, update)  # invalid choice or didn't solve it => undo
    #     return False
    #
    # def ValidOne(self, n, kee, update):
    #     self.board[kee[0]][kee[1]] = n
    #     del self.val[kee]
    #     i, j = kee
    #     for ind in self.val.keys():
    #         if n in self.val[ind]:
    #             if ind[0] == i or ind[1] == j or (ind[0] // 3, ind[1] // 3) == (i // 3, j // 3):
    #                 update[ind] = n
    #                 self.val[ind].remove(n)
    #                 if len(self.val[ind]) == 0:
    #                     return False
    #     return True
    #
    # def undo(self, kee, update):
    #     self.board[kee[0]][kee[1]] = "."
    #     for k in update:
    #         if k not in self.val:
    #             self.val[k] = update[k]
    #         else:
    #             self.val[k].append(update[k])
    #     return None
