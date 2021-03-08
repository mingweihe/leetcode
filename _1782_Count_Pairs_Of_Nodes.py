from collections import defaultdict


class Solution(object):
    def countPairs(self, n, edges, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        degree = [0] * (n+1)
        edge_cnt = defaultdict(int)
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
            edge_cnt[min(u, v), max(u, v)] += 1
        
        degree_sorted = sorted(degree[1:])
        ans = []
        for x in queries:
            # using two pointers to find the total number of pairs
            cnt, j = 0, n
            for i in xrange(n):
                while j - 1 > i and degree_sorted[i] + degree_sorted[j-1] > x:
                    j -= 1
                if i < j: cnt += n - j
                else: cnt += n - i - 1
            # exclude the number of the common pairs
            for (u, v), c in edge_cnt.items():
                before = degree[u] + degree[v]
                if before <= x: continue
                if before - c <= x: cnt -= 1
            ans += cnt,
        return ans
