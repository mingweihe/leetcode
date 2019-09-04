import heapq


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        heap = []
        intervals.sort(key=lambda x:x[0])
        for s, e in intervals:
            if heap and s >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, e)
        return len(heap)
