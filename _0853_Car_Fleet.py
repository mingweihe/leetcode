class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars = sorted(zip(position, speed))
        stack = []
        for i in xrange(len(cars)-1, -1, -1):
            p, s = cars[i]
            arrival_time = float(target - p) / s
            if not stack or arrival_time > stack[-1]:
                stack += arrival_time,
        return len(stack)
