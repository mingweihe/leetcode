import bisect
import collections
import random


class MajorityChecker(object):

    def __init__(self, arr):
        """
        :type arr: List[int]
        """
        # Random pick (non-deterministic) approach
        self.arr = arr
        self.a2i = collections.defaultdict(list)
        for i, x in enumerate(arr):
            self.a2i[x].append(i)

    def query(self, left, right, threshold):
        """
        :type left: int
        :type right: int
        :type threshold: int
        :rtype: int
        """
        for i in xrange(10):
            major = self.arr[random.randint(left, right)]
            l = bisect.bisect_left(self.a2i[major], left)
            r = bisect.bisect_right(self.a2i[major], right)
            if r - l >= threshold:
                return major
        return -1
        mid = (left + right) / 2
        self.query

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
