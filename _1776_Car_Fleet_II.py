class Solution(object):
    def getCollisionTimes(self, cars):
        """
        :type cars: List[List[int]]
        :rtype: List[float]
        """
        n, stack = len(cars), []
        res = [-1] * n
        for i in xrange(n-1, -1, -1):
            p, s = cars[i]
            while stack and (s <= cars[stack[-1]][1] or float(cars[stack[-1]][0]-p) / (s-cars[stack[-1]][1]) >= res[stack[-1]] > 0):
                stack.pop()
            if stack: res[i] = float(cars[stack[-1]][0]-p) / (s-cars[stack[-1]][1])
            stack += i,
        return res
