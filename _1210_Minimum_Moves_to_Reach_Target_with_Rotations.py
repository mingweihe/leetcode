import collections


class Solution(object):
    def minimumMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Approach 2 BFS
        n = len(grid)
        dq = collections.deque([[0, 0, 0]])
        visited = set()
        moves = 0
        while dq:
            for _ in xrange(len(dq)):
                i, j, v = dq.popleft()
                if (i, j, v) in visited:
                    continue
                visited.add((i, j, v))
                if i == n - 1 and j == n - 2 and v == 0:
                    return moves
                if v:
                    if i + 2 < n and grid[i + 2][j] == 0:
                        dq.append([i + 1, j, v])
                    if j + 1 < n and grid[i][j + 1] == 0 and grid[i + 1][j + 1] == 0:
                        dq.append([i, j + 1, v])
                        dq.append([i, j, 0])
                else:
                    if j + 2 < n and grid[i][j + 2] == 0:
                        dq.append([i, j + 1, v])
                    if i + 1 < n and grid[i + 1][j] == 0 and grid[i + 1][j + 1] == 0:
                        dq.append([i + 1, j, v])
                        dq.append([i, j, 1])
            moves += 1
        return -1

        # Approach 1 dynamic programming
        # n = len(grid)
        # grid.append([1]*n)
        # # record tails' status
        # dp = [[[float('inf')]*2 for _ in xrange(n+1)] for _ in xrange(n+1)]
        # dp[1][1][0] = 0
        # for i in xrange(1, n+1):
        #     for j in xrange(1, n):
        #         # tail check
        #         if grid[i-1][j-1] == 1: continue
        #         # head check
        #         if grid[i][j-1] == 0:
        #             dp[i][j][1] = min(dp[i][j][1], dp[i][j-1][1]+1, dp[i-1][j][1]+1)
        #         if grid[i-1][j] == 0:
        #             dp[i][j][0] = min(dp[i][j][0], dp[i-1][j][0]+1, dp[i][j-1][0]+1)
        #         if grid[i][j] == 0 and grid[i][j-1] == 0 and grid[i-1][j] == 0:
        #             dp[i][j][0] = min(dp[i][j][0], dp[i][j][1]+1)
        #             dp[i][j][1] = min(dp[i][j][1], dp[i][j][0]+1)
        # return -1 if dp[-1][-2][0] == float('inf') else dp[-1][-2][0]
