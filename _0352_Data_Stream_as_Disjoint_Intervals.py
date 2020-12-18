from bisect import insort


class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: None
        """
        insort(self.intervals, [val, val])
        

    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        res = []
        for s, e in self.intervals:
            if not res:
                res.append([s, e])
                continue
            if s - res[-1][1] < 2:
                res[-1][1] = max(res[-1][1], e)
            else:
                res.append([s, e])
        self.intervals = res
        return res
                
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
