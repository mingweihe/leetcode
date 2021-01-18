class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.maxSize = maxSize
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) < self.maxSize:
            self.stack += x,

    def pop(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack.pop()
        return -1
        
    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        for i in xrange(min(k, len(self.stack))):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
