class MinStack(object):
    class Node:
        def __init__(self, v):
            self.min = self.next = None
            self.val = v

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = None

    def push(self, x):
        if not self.head:
            self.head = self.Node(x)
            self.head.min = self.head
        else:
            t = self.head
            self.head = self.Node(x)
            self.head.next = t
            if x <= t.min.val:
                self.head.min = self.head
            else:
                self.head.min = t.min

    def pop(self):
        if self.head:
            self.head = self.head.next

    def top(self):
        if self.head:
            return self.head.val

    def getMin(self):
        if self.head:
            return self.head.min.val

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
