from collections import deque, defaultdict


class Solution(object):
    def frogPosition(self, n, edges, t, target):
        """
        :type n: int
        :type edges: List[List[int]]
        :type t: int
        :type target: int
        :rtype: float
        """
        qu = deque([[1, 1.0, 0]])
        visited = set([1])
        graph = defaultdict(list)
        for a, b in edges:
            graph[a] += b,
            graph[b] += a,
        while qu:
            v, p, time = qu.popleft()
            nexts = [x for x in graph[v] if x not in visited]
            if v == target and (time == t or (not nexts and time < t)):
                return p
            for nx_v in nexts:
                visited.add(nx_v)
                qu.append([nx_v, p / len(nexts), time + 1])
        return 0
