class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        dis, res = float('inf'), -1
        for i, (a, b) in enumerate(points):
            if a != x and b != y: continue
            cur = abs(a-x) + abs(b-y)
            if cur < dis:
                dis = cur
                res = i
        return res
