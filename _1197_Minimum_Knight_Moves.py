from collections import deque


class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # Approach 3 formula, time O(1)
        x, y = abs(x), abs(y)
        if x < y: x, y = y, x
        if x == 1 and y == 0: return 3
        if x == y == 2: return 4
        delta = x - y
        if y > delta: return delta - (((delta - y) / 3) << 1)
        return delta - (((delta - y) / 4) << 1)

        # Approach 2 dfs + cache,  time O(M*N)
        # cache = {(0, 0): 0, (1, 0): 3, (0, 1): 3}
        # def dfs(x, y):
        #     if (x, y) in cache: return cache[(x, y)]
        #     res = min(dfs(abs(x-1), abs(y-2)), dfs(abs(x-2), abs(y-1))) + 1
        #     cache[(x, y)] = res
        #     return res
        # return dfs(abs(x), abs(y))

        # Approach 1 bfs time O(M*N)
        # queue = deque([(0, 0)])
        # visited = set()
        # res = 0
        # cx, cy = 0, 0
        # x, y = abs(x), abs(y)
        # dirs = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2],
        #         [1, 2], [2, -1], [2, 1]]
        # while queue:
        #     for _ in xrange(len(queue)):
        #         cx, cy = queue.popleft()
        #         if cx == x and cy == y: return res
        #         for i, j in dirs:
        #             next_x, next_y = cx+i, cy+j
        #             next_coordi = (next_x, next_y)
        #             if next_coordi in visited: continue
        #             # pruning
        #             if -1 < next_x < x+2 and -1 < next_y < y+2:
        #                 queue.append(next_coordi)
        #                 visited.add(next_coordi)
        #     res += 1
        # return -1
