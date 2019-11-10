class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        rows = [0]*n
        cols = [0]*m
        for i, j in indices:
            rows[i] += 1
            cols[j] += 1
        res = 0
        for i in xrange(n):
            for j in xrange(m):
                res += (rows[i] + cols[j]) & 1
        return res
