from heapq import heappop, heappush


class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        ## approach 3, dijkstra
        hq = [(0, 0, 0)]
        dirs = [0, -1, 0, 1, 0]
        m, n = len(heights), len(heights[0])
        d_matrix = [[float('inf')] * n for _ in xrange(m)]
        d_matrix[0][0] = 0
        while hq:
            d, i, j = heappop(hq)
            for k in xrange(4):
                ni, nj = i + dirs[k], j + dirs[k+1]
                if ni < 0 or ni == m or nj < 0 or nj == n: continue
                neffort = max(d, abs(heights[ni][nj]-heights[i][j]))
                if neffort < d_matrix[ni][nj]:
                    d_matrix[ni][nj] = neffort
                    heappush(hq, (neffort, ni, nj))
        return d_matrix[-1][-1]
        
        ## approach 2, binary search
        # m, n = len(heights), len(heights[0])
        # dirs = [0, -1, 0, 1, 0]
        # def bfs(cost):
        #     seen = [[False] * n for _ in xrange(m)]
        #     seen[0][0] = True
        #     qu = deque()
        #     qu.append([0, 0])
        #     while qu:
        #         i, j = qu.popleft()
        #         for k in xrange(4):
        #             ni, nj = i + dirs[k], j + dirs[k+1]
        #             if ni < 0 or ni == m or nj < 0 or nj == n: continue
        #             if seen[ni][nj]: continue
        #             if abs(heights[ni][nj] - heights[i][j]) > cost: continue
        #             qu.append([ni, nj])
        #             seen[ni][nj] = True
        #     return seen[-1][-1]
        # l, r = 0, 10**6
        # while l < r:
        #     mid = l + (r-l) / 2
        #     if bfs(mid): r = mid
        #     else: l = mid + 1
        # return l
        
        ## approach 1, rolling dp
        # m, n = len(heights), len(heights[0])
        # if m == n == 1: return 0
        # dp = [[float('inf')] * n for _ in xrange(m)]
        # dp[0][0] = 0
        # dirs = [0, -1, 0, 1, 0]
        # for _ in xrange(max(m, n)):
        #     for i in xrange(m):
        #         for j in xrange(n):
        #             for k in xrange(4):
        #                 ni = i + dirs[k+1]
        #                 nj = j + dirs[k]
        #                 if nj < 0 or nj == n or ni < 0 or ni == m: continue
        #                 cur_effort = max(dp[ni][nj], abs(heights[i][j]-heights[ni][nj]))
        #                 dp[i][j] = min(dp[i][j], cur_effort)
        # return dp[m-1][n-1]
