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

        def flip(xmat, x, y):
            new_mat = copy.deepcopy(xmat)
            new_mat[x][y] ^= 1
            for x1, y1 in dirs:
                xn, yn = x + x1, y + y1
                if 0 <= xn < m and 0 <= yn < n:
                    new_mat[xn][yn] ^= 1
            return new_mat

        visited = set()
        queue = collections.deque([[mat, 0]])
        while queue:
            for _ in xrange(len(queue)):
                cmat, cnt = queue.popleft()
                if sum(map(sum, cmat)) == 0: return cnt
                for i in xrange(m):
                    for j in xrange(n):
                        nmat = flip(cmat, i, j)
                        cur = tuple(map(tuple, nmat))
                        if cur in visited: continue
                        queue.append([nmat, cnt + 1])
                        visited.add(cur)
        return -1

