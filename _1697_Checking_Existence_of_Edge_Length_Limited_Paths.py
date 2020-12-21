class Solution(object):
    def distanceLimitedPathsExist(self, n, edgeList, queries):
        """
        :type n: int
        :type edgeList: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        roots = range(n)
        def find(node):
            if roots[node] != node:
                roots[node] = find(roots[node])
            return roots[node]
        queries = sorted([[l, p, q, i] for i, (p, q, l) in enumerate(queries)])
        edgeList.sort(key = lambda x: x[2])
        res = [None] * len(queries)
        ii = 0
        for l, p, q, i in queries:
            while ii < len(edgeList) and edgeList[ii][2] < l:
                u, v, d = edgeList[ii]
                u = find(u)
                v = find(v)
                roots[u] = v
                ii += 1
            res[i] = find(p) == find(q)
        return res
