from collections import defaultdict


class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        graph = defaultdict(list)
        for i, x in enumerate(manager):
            graph[x] += i,
        def dfs(node, time):
            self.res = max(self.res, time)
            for nx in graph[node]:
                dfs(nx, time + informTime[node])
        self.res = 0
        dfs(headID, 0)
        return self.res
