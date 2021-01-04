class Solution(object):
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
            kruskal's minimum spanning tree algorithm
                (be careful about difference between n and the length of edges)
        """
        class UnionFind:
            def __init__(self):
                self.root = range(n)
            def find(self, x):
                if self.root[x] != x:
                    self.root[x] = self.find(self.root[x])
                return self.root[x]
            def union(self, a, b):
                na = self.find(a)
                nb = self.find(b)
                if na == nb: return False
                self.root[na] = nb
                return True
        
        def mst(edge_exclude=-1, edge_include=-1):
            uf = UnionFind()
            cost, count = 0, 0
            if edge_include >= 0:
                uf.union(edges[edge_include][1], edges[edge_include][2])
                cost += edges[edge_include][0]
                count += 1
            for i in xrange(len(edges)):
                if edge_exclude == i: continue
                if not uf.union(edges[i][1], edges[i][2]): continue
                cost += edges[i][0]
                count += 1
            if count == n - 1: return cost
            return float('inf')

        edges = sorted([[w, a, b, i] for i, (a, b, w) in enumerate(edges)])
        res = [[], []]
        min_cost = mst()
        for i in xrange(len(edges)):
            if mst(i) > min_cost: res[0] += edges[i][3],
            elif mst(-1, i) == min_cost: res[1] += edges[i][3],
        return res
