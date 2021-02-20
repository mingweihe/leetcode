from collections import deque


class Solution(object):
    def highestPeak(self, A):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        qu = deque()
        m, n = len(A), len(A[0])
        res = [[-1] * n for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if A[i][j]:
                    res[i][j] = 0
                    qu.append((i, j))
        dirs = [-1, 0, 1, 0, -1]
        while qu:
            for _ in xrange(len(qu)):
                i, j = qu.popleft()
                for k in xrange(4):
                    ni, nj = i + dirs[k], j + dirs[k+1]
                    if ni < 0 or nj < 0 or ni == m or nj == n: continue
                    if res[ni][nj] != -1: continue
                    res[ni][nj] = res[i][j] + 1
                    qu.append((ni, nj))
        return res
