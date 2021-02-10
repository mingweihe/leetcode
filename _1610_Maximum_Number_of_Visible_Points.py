import math
from collections import deque

class Solution(object):
    def visiblePoints(self, points, angle, location):
        """
        :type points: List[List[int]]
        :type angle: int
        :type location: List[int]
        :rtype: int
        """
        def get_angle(p):
            ans = math.atan2(p[1]-location[1], p[0]-location[0]) / (2*math.pi) * 360
            return ans
        angles = []
        same = 0
        max_len = 0
        for point in points:
            if point == location: same += 1
            else: angles += get_angle(point),
        angles.sort()
        dq = deque()
        for x in angles:
            dq.append(x)
            while x - dq[0] > angle:
                dq.popleft()
            max_len = max(max_len, len(dq))
        for x in angles:
            if x > angle: break
            x += 360
            dq.append(x)
            while x - dq[0] > angle:
                dq.popleft()
            max_len = max(max_len, len(dq))
        return same + max_len
