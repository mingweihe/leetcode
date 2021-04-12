#!/usr/bin/python3
from sortedcontainers import SortedList
from collections import deque
class MKAverage:

    def __init__(self, m: int, k: int):
        self.m, self.k = m, k
        self.sl = SortedList()
        self.dq = deque()
        self.total = 0
        self.ksmall = 0
        self.klarge = 0
        
    def addElement(self, num: int) -> None:
        # add number
        self.total += num
        self.dq.append(num)
        idx = self.sl.bisect_left(num)
        if idx < self.k:
            self.ksmall += num
            if len(self.sl) >= self.k:
                self.ksmall -= self.sl[self.k-1]
        
        if idx >= len(self.sl) - self.k + 1:
            self.klarge += num
            if len(self.sl) >= self.k:
                self.klarge -= self.sl[-self.k]
        self.sl.add(num)
        # remove number
        if len(self.dq) <= self.m: return
        num = self.dq.popleft()
        self.total -= num
        idx = self.sl.bisect_left(num)
        if idx < self.k:
            self.ksmall -= num
            self.ksmall += self.sl[self.k]
        if idx >= len(self.sl) - self.k:
            self.klarge -= num
            self.klarge += self.sl[-self.k-1]
        self.sl.remove(num)

    def calculateMKAverage(self) -> int:
        if len(self.dq) < self.m: return -1
        return (self.total - self.ksmall - self.klarge) // (self.m - 2 * self.k)

# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
