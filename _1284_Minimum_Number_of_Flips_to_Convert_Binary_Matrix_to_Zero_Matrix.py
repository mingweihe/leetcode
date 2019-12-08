import collections
import copy


class Solution(object):
    def minFlips(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        m, n = len(mat), len(mat[0])

        def opposite(num):
            return num & 1 ^ 1

        def tostr(xmat):
            res = []
            for i in xrange(m):
                for j in xrange(n):
                    res += str(xmat[i][j]),
            return ''.join(res)

        def flip(xmat, x, y):
            new_mat = copy.deepcopy(xmat)
            new_mat[x][y] = opposite(new_mat[x][y])
            for x1, y1 in dirs:
                xn, yn = x + x1, y + y1
                if 0 <= xn < m and 0 <= yn < n:
                    new_mat[xn][yn] = opposite(new_mat[xn][yn])
            return new_mat

        def valid(xmat):
            ans = 0
            for i in xrange(m):
                for j in xrange(n):
                    ans += xmat[i][j]
            return ans == 0

        visited = set()
        queue = collections.deque([[mat, 0]])
        while queue:
            for _ in xrange(len(queue)):
                cmat, cnt = queue.popleft()
                if valid(cmat): return cnt
                for i in xrange(m):
                    for j in xrange(n):
                        nmat = flip(cmat, i, j)
                        cur = tostr(nmat)
                        if cur in visited: continue
                        queue.append([nmat, cnt + 1])
                        visited.add(cur)
        return -1
