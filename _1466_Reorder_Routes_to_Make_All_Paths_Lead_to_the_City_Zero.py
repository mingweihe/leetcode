from collections import defaultdict, deque


class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)
        dirs = set()
        for a, b in connections:
            graph[a] += b,
            graph[b] += a,
            dirs.add((a, b))
        qu = deque([0])
        seen = {0}
        res = 0
        while qu:
            node = qu.popleft()
            for nx in graph[node]:
                if nx in seen: continue
                seen.add(nx)
                qu.append(nx)
                if (nx, node) not in dirs:
                    res += 1
        return res
