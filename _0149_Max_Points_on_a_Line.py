class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
            simple implementing quiz
            keypoints: same points, same x point, same slope points
        """
        if not points: return 0
        # gcd = math.gcd # for python3

        def gcd(a, b):
            # while a: a, b = b % a, a
            # return b
            if a == 0: return b
            return gcd(b % a, a)
        res = 0
        L = len(points)
        for i in xrange(L):
            same_points = same_x_points = 1
            dic = {}
            for j in xrange(L):
                if i != j:
                    if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                        same_points += 1
                    if points[i][0] == points[j][0]:
                        same_x_points += 1
                    else:
                        x, y = points[i][0]-points[j][0], points[i][1]-points[j][1]
                        cd = gcd(x, y)
                        # -1/2 1/-2 can always be defeat by a farthest point
                        key = '{}/{}'.format(x/cd, y/cd)
                        dic[key] = dic.get(key, 0) + 1
                        res = max(res, dic[key]+same_points)
            res = max(res, same_x_points)
        return res
