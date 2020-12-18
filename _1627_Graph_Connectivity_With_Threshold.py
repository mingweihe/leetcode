class Solution(object):
    def areConnected(self, n, threshold, queries):
        """
        :type n: int
        :type threshold: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        def ufind(parents, n):
            if parents[n] == -1:
                return n
            parents[n] = ufind(parents, parents[n])
            return parents[n]
            
        parents = [-1] * (n + 1)
        for i in xrange(threshold+1, n+1):
            for j in xrange(i*2, n+1, i):
                xx = ufind(parents, i)
                yy = ufind(parents, j)
                if xx != yy: parents[xx] = yy
        
        res = []
        for i, j in queries:
            xx = ufind(parents, i)
            yy = ufind(parents, j)
            res += xx == yy,
        return res
