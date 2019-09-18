class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
            alternately, iters could be replaced by two lists
            length of iterator could also be replaced by a variable in a
            corresponding tuple.
        """
        self.A = []
        if v1: self.A.append(iter(v1))
        if v2: self.A.append(iter(v2))

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            it = self.A.pop(0)
            res = next(it)
            if it.__length_hint__() > 0:
                self.A.append(it)
            return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.A) != 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
