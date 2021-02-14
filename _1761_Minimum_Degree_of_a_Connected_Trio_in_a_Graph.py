class Solution(object):
    def minTrioDegree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        ## Approach 2, adjacent matrix
        deg = [0] * n
        A = [[False] * n for _ in xrange(n)]
        for u, v in edges:
            u, v = u-1, v-1
            deg[u] += 1
            deg[v] += 1
            A[u][v] = A[v][u] = True
        res = float('inf')
        for i in xrange(n-2):
            for j in xrange(i+1, n-1):
                if not A[i][j]: continue
                for k in xrange(j+1, n):
                    if A[i][k] and A[j][k]:
                        res = min(res, deg[i]+deg[j]+deg[k]-6)
        return -1 if res == float('inf') else res
        
        ## Approach 1, adjacent list
#         graph = defaultdict(set)
#         for u, v in edges:
#             graph[u].add(v)
#             graph[v].add(u)
#         res = float('inf')
#         ## way 1
#         for u, v in edges:
#             for x in graph[u] & graph[v]:
#                 res = min(res, len(graph[u]) + len(graph[v]) + len(graph[x]) - 6)
                
#         ## way 2
#         # for i in xrange(1, n):
#         #     for j in xrange(i+1, n+1):
#         #         if i not in graph[j]: continue
#         #         for k in graph[i] & graph[j]:
#         #             cur = len(graph[i]) + len(graph[j]) + len(graph[k]) - 6
#         #             res = min(res, cur)
#         return -1 if res == float('inf') else res
