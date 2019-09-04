class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.s.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        aS = []
        while len(self.s) > 1:
            aS.append(self.s.pop())
        res = self.s.pop()
        while aS: self.s.append(aS.pop())
        return res

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        aS = []
        top = None
        while self.s:
            top = self.s.pop()
            aS.append(top)
        while aS: self.s.append(aS.pop())
        return top

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.s) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
