class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        ss = set()
        mini, maxi = float('inf'), float('-inf')
        for x, y in points:
            ss.add((x, y))
            mini = min(x, mini)
            maxi = max(x, maxi)
        L = mini + maxi
        for x, y in points:
            if (L - x, y) not in ss: return False
        return True
