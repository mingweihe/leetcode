class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Approach 2
        row, col = map(max, grid), map(max, zip(*grid))
        return sum(min(x, y) for x in row for y in col) - sum(map(sum, grid))
        # Approach 1
        # rows_max = [max(x) for x in grid]
        # cols_max = [max(x) for x in zip(*grid)]
        # res = 0
        # for i in xrange(len(grid)):
        #     for j in xrange(len(grid[0])):
        #         add = min(rows_max[i], cols_max[j]) - grid[i][j]
        #         res += 0 if add < 0 else add
        # return res
