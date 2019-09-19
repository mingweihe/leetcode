class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
            the purpose of this puzzle is to find the minimum manhattan distance
            so we don't need to find the meeting point.
            then we have the following trick
        """
        if not grid: return 0
        Xs, Ys = [], []
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == 1:
                    Xs += i,
        # optional: Xs.sort(), Ys.sort()
        for j in xrange(len(grid[0])):
            for i in xrange(len(grid)):
                if grid[i][j] == 1:
                    Ys += j,
        return self.minimum(Xs) + self.minimum(Ys)

    def minimum(self, A):
        res, i, j = 0, 0, len(A) - 1
        while i < j:
            res += A[j] - A[i]
            i, j = i + 1, j - 1
        return res
