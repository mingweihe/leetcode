class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ## Approach 2, O(m*n)
        m, n = len(matrix), len(matrix[0])
        min_rows = [float('inf')] * m
        max_cols = [float('-inf')] * n
        for i in xrange(m):
            for j in xrange(n):
                min_rows[i] = min(min_rows[i], matrix[i][j])
                max_cols[j] = max(max_cols[j], matrix[i][j])
        res = []
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == min_rows[i] == max_cols[j]:
                    res += matrix[i][j],
        return res
    
        ## Approach 1, brute force, O(m*n*(m+n))
        # m, n = len(matrix), len(matrix[0])
        # res = []
        # for i in xrange(m):
        #     for j in xrange(n):
        #         flag = True
        #         for k in xrange(m):
        #             if matrix[i][j] < matrix[k][j]:
        #                 flag = False
        #                 break
        #         if flag:
        #             for k in xrange(n):
        #                 if matrix[i][j] > matrix[i][k]:
        #                     flag = False
        #                     break
        #         if flag:
        #             res += matrix[i][j],
        # return res
