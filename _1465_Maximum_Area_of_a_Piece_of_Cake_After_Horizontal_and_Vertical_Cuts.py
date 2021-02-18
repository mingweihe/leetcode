class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        horizontalCuts.sort()
        verticalCuts.sort()
        width, height = 0, 0
        last = 0
        for x in verticalCuts:
            width = max(width, x-last)
            last = x
        width = max(width, w-last)
        last = 0
        for x in horizontalCuts:
            height = max(height, x-last)
            last = x
        height = max(height, h-last)
        return width * height % (10**9 + 7)
