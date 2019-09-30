import collections


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        res = []
        graph = collections.defaultdict(list)
        for i, (x, y) in enumerate(equations):
            graph[x].append([y, values[i]])
            graph[y].append([x, 1 / values[i]])
        for x, y in queries:
            res.append(self.find(graph, x, y, 1, set()))
        return res

    def find(self, graph, x, y, val, visited):
        if x not in graph or y not in graph: return -1
        if x in visited: return -1
        if x == y: return val
        visited.add(x)
        for v in graph[x]:
            sub_rs = self.find(graph, v[0], y, val * v[1], visited)
            if sub_rs != -1: return sub_rs
        visited.discard(x)
        return -1
