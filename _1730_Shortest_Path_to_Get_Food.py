from collections import deque


class Solution(object):
    def getFood(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        dq = deque()
        seen = set()
        dirs = [-1, 0, 1, 0, -1]
        m, n = len(grid), len(grid[0])
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '*':
                    dq.append([i, j])
                    seen.add((i, j))
        ans = 0
        while dq:
            for _ in xrange(len(dq)):
                i, j = dq.popleft()
                if grid[i][j] == '#': return ans
                for k in xrange(4):
                    ni, nj = i + dirs[k], j + dirs[k+1]
                    if ni < 0 or ni == m or nj < 0 or nj == n: continue
                    if grid[ni][nj] == 'X': continue
                    if (ni, nj) in seen: continue
                    seen.add((ni, nj))
                    dq.append([ni, nj])
            ans += 1
        return -1
