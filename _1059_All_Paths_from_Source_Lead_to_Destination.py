from collections import defaultdict


class Solution(object):
    def leadsToDestination(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
            points: circle detection in a directed graph
        """
        def dfs(node):
            if not graph[node]:
                if node == destination: return True
                else: return False
            if node in seen: return False
            seen.add(node)
            for nx in graph[node]:
                if not dfs(nx): return False
            seen.discard(node)
            return True
        
        graph = defaultdict(list)
        seen = set()
        for u, v in edges:
            graph[u] += v,
        return dfs(source)
