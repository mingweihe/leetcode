from heapq import heappush, heappop


class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        hq = []
        for i in xrange(len(heights)-1):
            d = heights[i+1] - heights[i]
            if d > 0: heappush(hq, d)
            if len(hq) > ladders: bricks -= heappop(hq)
            if bricks < 0: return i
        return len(heights) - 1
