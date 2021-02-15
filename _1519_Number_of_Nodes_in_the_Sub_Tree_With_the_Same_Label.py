from collections import defaultdict


class Solution(object):
    def countSubTrees(self, n, edges, labels):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :rtype: List[int]
        """
        def dfs(node, seen):
            if node in seen: return {}
            seen.add(node)
            ans = defaultdict(int)
            for nx in graph[node]:
                cur = dfs(nx, seen)
                for k, v in cur.items():
                    ans[k] += v
            ans[labels[node]] += 1
            res[node] = ans[labels[node]]
            return ans
            
        graph = defaultdict(list)
        for a, b in edges:
            graph[a] += b,
            graph[b] += a,
        res = defaultdict(int)
        dfs(0, set())
        return [res[i] for i in xrange(n)]
