class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
            counter-intuitive thought:
                find a to b, which also means find b to a
        """

        # Approach 2 dfs
        def dfs(i, j, dis):
            if i < 0 or i == len(rooms) or j < 0 \
                    or j == len(rooms[0]) or rooms[i][j] < dis:
                return
            rooms[i][j] = dis
            dfs(i + 1, j, dis + 1)
            dfs(i - 1, j, dis + 1)
            dfs(i, j + 1, dis + 1)
            dfs(i, j - 1, dis + 1)

        for i in xrange(len(rooms)):
            for j in xrange(len(rooms[0])):
                if rooms[i][j] == 0:
                    dfs(i, j, 0)

        # Approach 1 bfs
        # inf, queue = (1<<31)-1, []
        # for i in xrange(len(rooms)):
        #     for j in xrange(len(rooms[0])):
        #         if rooms[i][j] == 0:
        #             queue.append([i, j])
        # while queue:
        #     i, j = queue.pop(0)
        #     if i+1 < len(rooms) and rooms[i+1][j] == inf:
        #         rooms[i+1][j] = rooms[i][j] + 1
        #         queue.append((i+1, j))
        #     if i-1 > -1 and rooms[i-1][j] == inf:
        #         rooms[i-1][j] = rooms[i][j] + 1
        #         queue.append((i-1, j))
        #     if j+1 < len(rooms[0]) and rooms[i][j+1] == inf:
        #         rooms[i][j+1] = rooms[i][j] + 1
        #         queue.append((i, j+1))
        #     if j-1 > -1 and rooms[i][j-1] == inf:
        #         rooms[i][j-1] = rooms[i][j] + 1
        #         queue.append((i, j-1))
