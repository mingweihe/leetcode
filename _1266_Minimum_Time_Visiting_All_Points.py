class Solution(object):
    def minTimeToVisitAllPoints(self, P):
        """
        :type P: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in xrange(1, len(P)):
            res += max(abs(P[i][0]-P[i-1][0]), abs(P[i][1]-P[i-1][1]))
        return res
