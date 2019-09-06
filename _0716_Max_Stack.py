class MaxStack(object):
    # because the existence of popMax operation
    # we can't make maximum operation at O(1) time complexity
    # O(log(n)) is what we can do
    class Node(object):
        def __init__(self, val):
            self.val = val
            self.prev = self.next = None

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = None
        self.seq = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        node = self.Node(x)
        if not self.stack:
            self.stack = node
            self.seq = [node]
        else:
            node.next = self.stack
            self.stack.prev = node
            self.stack = node
            left, right = 0, len(self.seq) - 1
            while left <= right:
                mid = (left + right) / 2
                if x >= self.seq[mid].val:
                    right = mid - 1
                else:
                    left = mid + 1
            self.seq.insert(left, node)

    def pop(self):
        """
        :rtype: int
        """
        node = self.stack
        self.stack = self.stack.next
        if self.stack:
            self.stack.prev = None
        left, right = 0, len(self.seq) - 1
        while left <= right:
            mid = (left + right) / 2
            if node.val >= self.seq[mid].val:
                right = mid - 1
            else:
                left = mid + 1
        self.seq.pop(left)
        return node.val

    def top(self):
        # self._print_seq()
        # self._print_stack()
        """
        :rtype: int
        """
        return self.stack.val

    def peekMax(self):
        """
        :rtype: int
        """
        return self.seq[0].val

    def popMax(self):
        """
        :rtype: int
        """
        node = self.seq.pop(0)
        if node is self.stack:
            self.stack = self.stack.next
            if self.stack:
                self.stack.prev = None
        else:
            node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
        return node.val

    def _print_seq(self):
        res = ''
        for x in self.seq:
            res += str(x.val) + '->'
        print(res)

    def _print_stack(self):
        res = ''
        node = self.stack
        while node:
            res += str(node.val) + '->'
            node = node.next
        print(res)
# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
