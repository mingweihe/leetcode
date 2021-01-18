from bisect import bisect_left, bisect_right


class RangeModule(object):

    def __init__(self):
        self.data = []

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        start = bisect_left(self.data, left)
        end = bisect_right(self.data, right)
        subtrack = []
        if start % 2 == 0:
            subtrack += left,
        if end % 2 == 0:
            subtrack += right,
        self.data[start:end] = subtrack

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        start = bisect_right(self.data, left)
        end = bisect_left(self.data, right)
        return start == end and start % 2 == 1
        
    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        
        start = bisect_left(self.data, left)
        end = bisect_right(self.data, right)
        subtrack = []
        if start % 2 == 1:
            subtrack += left,
        if end % 2 == 1:
            subtrack += right,
        self.data[start:end] = subtrack

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
