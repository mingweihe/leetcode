class Solution(object):
    def checkStraightLine(self, coors):
        """
        :type coors: List[List[int]]
        :rtype: bool
        """
        (x0, y0), (x1, y1) = coors[:2]
        for i in xrange(2, len(coors)):
            xi, yi = coors[i]
            if (y1 - y0) * (xi - x0) != (yi - y0) * (x1 - x0):
                return False
        return True
