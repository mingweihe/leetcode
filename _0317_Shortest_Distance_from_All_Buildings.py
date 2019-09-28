import collections
dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]


class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
            Just simply bfs traverse all, time O(m^2*n^n)
            Calculate all empy land total distances to all buildings
        """
        m, n = len(grid), len(grid[0])
        dists = [[0] * n for _ in xrange(m)]
        nums = [[0] * n for _ in xrange(m)]
        num_buildings = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    num_buildings += 1
                    self.bfs(dists, nums, i, j, grid)
        res = float('inf')
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 0 and nums[i][j] == num_buildings:
                    res = min(res, dists[i][j])
        return -1 if res == float('inf') else res

    def bfs(self, dists, nums, row, col, grid):
        visited = set()
        m, n = len(dists), len(dists[0])
        queue = collections.deque([[row, col]])
        distance = 0
        while queue:
            distance += 1
            for _ in xrange(len(queue)):
                x, y = queue.popleft()
                for i, j in dirs:
                    nx, ny = x + i, y + j
                    if 0 <= nx < m and 0 <= ny < n \
                            and grid[nx][ny] == 0 and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append([nx, ny])
                        dists[nx][ny] += distance
                        nums[nx][ny] += 1
