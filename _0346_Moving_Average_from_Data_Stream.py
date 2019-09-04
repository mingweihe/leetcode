from collections import deque


class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.dq = deque([], size)
        self.summ = .0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.dq) == self.dq.maxlen:
            self.summ -= self.dq.popleft()
        self.summ += val
        self.dq.append(val)
        return self.summ / len(self.dq)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
