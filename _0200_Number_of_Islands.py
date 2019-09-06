class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # Approach 2
        def sink(i, j):
            if -1 < i < len(grid) and -1 < j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0'
                # map in python3 is lazy excution mode, while python2 is eager
                map(sink, [i, i, i + 1, i - 1], [j + 1, j - 1, j, j])
                return 1
            return 0
        return sum(sink(i, j) for i in xrange(len(grid)) for j in xrange(len(grid[i])))

        # Approach 1
        # H = len(grid)
        # if H == 0: return 0
        # W = len(grid[0])
        # dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        # cnt = 0
        # for i in xrange(H):
        #     for j in xrange(W):
        #         if grid[i][j] == '1':
        #             cnt += 1
        #             stack = [(i,j)]
        #             while stack:
        #                 y, x = stack.pop()
        #                 grid[y][x] = '0'
        #                 for m, n in dirs:
        #                     y_m, x_n = y+m, x+n
        #                     if -1<y_m<H and -1<x_n<W and grid[y_m][x_n] == '1':
        #                         stack.append((y_m, x_n))
        # return cnt
