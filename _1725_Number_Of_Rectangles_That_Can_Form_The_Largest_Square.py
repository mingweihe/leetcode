from collections import Counter


class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        return max(Counter(map(min, rectangles)).items())[1]
