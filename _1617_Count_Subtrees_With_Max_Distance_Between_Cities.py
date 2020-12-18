from collections import defaultdict, deque


class Solution(object):
    def countSubgraphsForEachDiameter(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        dCounts = defaultdict(int)
        for u, v in edges:
            graph[u-1] += v-1,
            graph[v-1] += u-1,
        
        def bfs(start, subtree):
            max_height = -1
            max_height_node = -1
            qu = deque()
            qu.append(start)
            seen = {start}
            while qu:
                qu_next = deque()
                max_height_node = qu[-1]
                for node in qu:
                    for nei in graph[node]:
                        if 1 << nei & subtree == 0: continue
                        if nei in seen: continue
                        seen.add(nei)
                        qu_next.append(nei)
                qu = qu_next
                max_height += 1
            seen_tree = sum(1 << i for i in seen)
            if seen_tree != subtree: return 0, 0
            return max_height_node, max_height

        skips = {1 << i for i in xrange(n+1)}
        for i in xrange(1, 2**n):
            if i in skips: continue
            for j in xrange(1, n+1):
                if 1 << j & i:
                    v, h = bfs(j, i)
                    if h == 0: continue
                    v, h = bfs(v, i)
                    dCounts[h] += 1
                    break
        return [dCounts[i] for i in xrange(1, n)]
