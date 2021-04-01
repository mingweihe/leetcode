class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        ## Approach 3, union find / disjoint set
        def find(x):
            if x != roots[x]:
                roots[x] = find(roots[x])
            return roots[x]
        roots = range(len(graph))
        for u in xrange(len(graph)):
            pu = find(u)
            for v in graph[u]:
                p0, pv = find(graph[u][0]), find(v)
                if pv == pu: return False
                roots[pv] = roots[p0]
        return True
    
        ## Approach 2, BFS
        # colors = [0] * len(graph)
        # for i in xrange(len(graph)):
        #     if colors[i] != 0: continue
        #     colors[i] = 1
        #     dq = deque()
        #     dq.append(i)
        #     while dq:
        #         node = dq.popleft()
        #         for nx in graph[node]:
        #             if colors[nx] == colors[node]: return False
        #             elif colors[nx] == 0:
        #                 colors[nx] = -colors[node]
        #                 dq.appendleft(nx)
        # return True
        
#         # Approach 1, DFS
#         def valid(x, c):
#             if x in colors:
#                 if colors[x] != c: return False
#                 else: return True
#             colors[x] = c
#             for nx in graph[x]:
#                 if not valid(nx, c^1): return False
#             return True
            
#         colors = {}
#         for node in xrange(len(graph)):
#             if node not in colors and not valid(node, 0): return False
#         return True
