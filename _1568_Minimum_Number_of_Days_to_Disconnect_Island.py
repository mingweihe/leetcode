class Solution(object):
    def minDays(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(i, j, seen):
            if i < 0 or i == m or j < 0 or j == n: return
            if grid[i][j] == 0: return
            if (i, j) in seen: return
            seen.add((i, j))
            for k in xrange(4):
                dfs(i+dirs[k], j+dirs[k+1], seen)
            
        def is_disconnected():
            num_island = 0
            start_i, start_j = 0, 0
            for i in xrange(m):
                for j in xrange(n):
                    if grid[i][j] == 1:
                        num_island += 1
                        start_i, start_j = i, j
            if num_island == 0: return True
            seen = set()
            dfs(start_i, start_j, seen)
            if num_island != len(seen): return True
            return False
        
        dirs = [-1, 0, 1, 0, -1]
        m, n = len(grid), len(grid[0])
        if is_disconnected(): return 0
        
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if is_disconnected(): return 1
                    grid[i][j] = 1
        return 2
