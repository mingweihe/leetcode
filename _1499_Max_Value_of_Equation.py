from collections import deque


class Solution(object):
    def findMaxValueOfEquation(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        res = float('-inf')
        dq = deque()
        for x, y in points:
            while dq and x - dq[0][0] > k:
                dq.popleft()
            res = max(res, y+x+dq[0][1] if dq else float('-inf'))
            while dq and y-x > dq[-1][1]:
                dq.pop()            
            dq.append([x, y-x])
        return res
