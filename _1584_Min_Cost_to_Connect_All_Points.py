class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        parents = range(n)
        def find(node):
            if node != parents[node]:
                parents[node] = find(parents[node])
            return parents[node]

        costs = []
        for i in xrange(n-1):
            for j in xrange(i+1, n):
                costs += [abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1]), i, j],
        costs.sort()
        res = 0
        for d, i, j in costs:
            a, b = find(i), find(j)
            if a == b: continue
            parents[a] = b
            res += d
        return res
