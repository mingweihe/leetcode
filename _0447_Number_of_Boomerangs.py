class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # Approach 2
        res = 0
        for [x1, y1] in points:
            d = {}
            for [x2, y2] in points:
                distance = (x1-x2)**2+(y1-y2)**2
                if distance in d:
                    res += d[distance]
                    d[distance] += 1
                else: d[distance] = 1
        return res*2

        # Approach 1
        # n, res = len(points), 0
        # for i in range(n):
        #     for j in range(n):
        #         for k in range(n):
        #             if i != j and i !=k and j !=k:
        #                 if (points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2 == \
        #                 (points[i][0]-points[k][0])**2+(points[i][1]-points[k][1])**2:
        #                     res += 1
        # return res
