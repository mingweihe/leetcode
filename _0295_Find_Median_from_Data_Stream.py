# from Queue import PriorityQueue
import heapq


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # self.small = PriorityQueue()
        # self.large = PriorityQueue()
        self.small = []
        self.large = []
        heapq.heapify(self.small)
        heapq.heapify(self.large)

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        min_large = heapq.heappushpop(self.large, num)
        heapq.heappush(self.small, -min_large)
        if len(self.small) > len(self.large):
            heapq.heappush(self.large, -heapq.heappop(self.small))
        # self.large.put(num)
        # self.small.put(-self.large.get())
        # if self.small.qsize() > self.large.qsize():
        #     self.large.put(-self.small.get())

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.large) > len(self.small):
            return self.large[0]
        return (self.large[0] - self.small[0]) / 2.

        # min_from_large = self.large.get()
        # self.large.put(min_from_large)
        # if self.large.qsize() > self.small.qsize():
        #     return min_from_large
        # max_from_small = self.small.get()
        # self.small.put(max_from_small)
        # return (min_from_large-max_from_small) / 2.

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
