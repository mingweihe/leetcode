# import numpy as np
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        # Approach 6 using two tables, optimized with three loops
        table_A, table_B = {}, {}
        for i in xrange(len(A)):
            table_A[i] = {}
            for j in xrange(len(A[0])):
                if A[i][j]: table_A[i][j] = A[i][j]
        for i in xrange(len(B[0])):
            table_B[i] = {}
            for j in xrange(len(B)):
                if B[j][i]: table_B[i][j] = B[j][i]
        res = [[0 for _ in xrange(len(B[0]))] for _ in xrange(len(A))]
        for i, row_A in table_A.items():
            for m, a in row_A.items():
                for j, col_B in table_B.items():
                    b = col_B.get(m)
                    if b: res[i][j] += a * b
        return res

        # Approach 5 using two tables,
        # which saving memories cost as sparse matrix contains lots of zeros.
        # table_A, table_B = {}, {}
        # for i in xrange(len(A)):
        #     table_A[i] = {}
        #     for j in xrange(len(A[0])):
        #         if A[i][j]: table_A[i][j] = A[i][j]
        # for i in xrange(len(B[0])):
        #     table_B[i] = {}
        #     for j in xrange(len(B)):
        #         if B[j][i]: table_B[i][j] = B[j][i]
        # res = [[0 for _ in xrange(len(B[0]))] for _ in xrange(len(A))]
        # for i, row_A in table_A.items():
        #     for m, a in row_A.items():
        #         for j, col_B in table_B.items():
        #             for n, b in col_B.items():
        #                 if m == n: res[i][j] += a*b
        # return res

        # Approach 4 optimized before both bottom two loops
        # m, n, commonL = len(A), len(B[0]), len(A[0])
        # res = [[0]*n for _ in xrange(m)]
        # for i in xrange(m):
        #     for k in xrange(commonL):
        #         if A[i][k]:
        #             for j in xrange(n):
        #                 if B[k][j]:
        #                     res[i][j] += A[i][k]*B[k][j]
        # return res

        # Approach 3 optimized at bottom if else
        # m, n, commonL = len(A), len(B[0]), len(A[0])
        # res = [[0]*n for _ in xrange(m)]
        # for i in xrange(m):
        #     for j in xrange(n):
        #         for k in xrange(commonL):
        #             if A[i][k] and B[k][j]:
        #                 res[i][j] += A[i][k]*B[k][j]
        # return res

        # Approach 2 naive computation
        # m, n, commonL = len(A), len(B[0]), len(A[0])
        # res = [[0]*n for _ in xrange(m)]
        # for i in xrange(m):
        #     for j in xrange(n):
        #         for k in xrange(commonL):
        #             res[i][j] += A[i][k]*B[k][j]
        # return res

        # Approach 1 numpy.matmul
        # return np.matmul(A, B).tolist()
