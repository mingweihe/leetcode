from collections import defaultdict


class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        boxes = defaultdict(int)
        for i in xrange(lowLimit, highLimit+1):
            cur = 0
            while i:
                cur += i % 10
                i /= 10
            boxes[cur] += 1
        return max(boxes.values())
