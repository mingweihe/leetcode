class Solution(object):
    def minimumOperationsToWriteY(self, g):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ys, non_ys = dict(), dict()
        n = len(g)
        comb = [[0, 1], [0, 2], [1, 2], [1, 0], [2, 0], [2, 1]]
        def cost(y_d, non_y_d):
            cnt = 0
            for x in {0, 1, 2} - {y_d}:
                cnt += ys.get(x, 0)
            for x in {0, 1, 2} - {non_y_d}:
                cnt += non_ys.get(x, 0)
            return cnt
        def is_write_y(ii, jj):
            if ii == jj and ii <= n//2: return True
            if ii + jj == n - 1 and ii <= n//2: return True
            if ii >= n//2 and jj == n//2: return True
            return False

        for i in xrange(n):
            for j in xrange(n):
                if is_write_y(i, j):
                    ys[g[i][j]] = ys.get(g[i][j], 0) + 1
                else:
                    non_ys[g[i][j]] = non_ys.get(g[i][j], 0) + 1

        res = float('inf')
        for y, non_y in comb:
            res = min(res, cost(y, non_y))
        return res
