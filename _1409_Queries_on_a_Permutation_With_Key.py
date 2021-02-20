class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        P = range(1, m+1)
        res = []
        for x in queries:
            res += P.index(x),
            P = [x] + P[:res[-1]] + P[res[-1]+1:]
        return res
