class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # Approach 2 disjoint sets
        if n - 1 != len(edges): return False

        def find(vs, v):
            while vs[v] != -1:
                v = vs[v]
            return v

        vertices = [-1] * n
        for v1, v2 in edges:
            v1 = find(vertices, v1)
            v2 = find(vertices, v2)
            if v1 == v2: return False
            vertices[v1] = v2
        return True

        # Approach 1 dfs
        # def dfs(gs, vis, cur_v, parent):
        #     adjacencies = gs[cur_v]
        #     for v in adjacencies:
        #         if v == parent: continue
        #         if v in vis: return False
        #         vis.add(v)
        #         cur_res = dfs(gs, vis, v, cur_v)
        #         if not cur_res: return False
        #     return True
        # graph = [[] for _ in xrange(n)]
        # for v1, v2 in edges:
        #     graph[v1].append(v2)
        #     graph[v2].append(v1)
        # visited = set([0])
        # res = dfs(graph, visited, 0, -1)
        # if not res: return False
        # return len(visited) == n
