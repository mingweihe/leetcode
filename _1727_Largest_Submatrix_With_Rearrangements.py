from collections import defaultdict


class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        d = defaultdict(list)
        m, n = len(matrix), len(matrix[0])
        for j in xrange(n):
            cur = 0
            for i in xrange(m):
                if matrix[i][j]:
                    cur += 1
                    d[i] += cur,
                else:
                    cur = 0
        res = 0
        for v in d.values():
            for i, x in enumerate(sorted(v, reverse=True)):
                res = max(res, (i+1) * x)
        return res
