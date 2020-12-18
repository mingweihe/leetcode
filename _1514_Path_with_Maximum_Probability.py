import collections


class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """
        graph = collections.defaultdict(list)
        for i, (a, b) in enumerate(edges):
            graph[a] += [b, succProb[i]],
            graph[b] += [a, succProb[i]],
        seen = collections.defaultdict(float)
        qu = collections.deque([[start, 1]])
        res = 0
        while qu:
            node, p = qu.popleft()
            if node == end:
                res = max(res, p)
                continue
            for next_n, next_p in graph[node]:
                new_next_p = next_p * p
                if new_next_p <= seen[next_n]: continue
                seen[next_n] = new_next_p
                qu.append([next_n, new_next_p])
        return res
