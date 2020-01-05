import collections


class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
            Tarjan bridges algorithm
            Time complexity O(V+E)
        """
        ids = [0] * n
        low_links = [0] * n
        visited = [False] * n
        res = []
        graph = collections.defaultdict(list)
        for a, b in connections:
            graph[a] += b,
            graph[b] += a,
        self.id = 0

        def dfs(node, parent):
            visited[node] = True
            ids[node] = low_links[node] = self.id
            self.id += 1
            for vertex in graph[node]:
                if vertex == parent: continue
                if not visited[vertex]:
                    dfs(vertex, node)
                    low_links[node] = min(low_links[node], low_links[vertex])
                    if ids[node] < low_links[vertex]:
                        res.append([node, vertex])
                else:
                    low_links[node] = min(low_links[node], ids[vertex])
        dfs(0, -1)
        return res
