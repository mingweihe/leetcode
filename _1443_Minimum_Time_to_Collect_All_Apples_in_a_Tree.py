from collections import defaultdict


class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        def dfs(node, time):
            if node in seen: return 0
            seen.add(node)
            ans = 0
            for nx in graph[node]:
                ans += dfs(nx, 1)
            if ans == 0:
                if hasApple[node]: return time
                else: return 0
            return ans + time
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a] += b,
            graph[b] += a,
        seen = set()
        return dfs(0, 0) * 2
