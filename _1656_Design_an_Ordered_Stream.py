class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.ptr = 1
        self.data = [None] * n
        

    def insert(self, id, value):
        """
        :type id: int
        :type value: str
        :rtype: List[str]
        """
        self.data[id-1] = value
        if self.ptr != id: return []
        res = []
        idx = id - 1
        
        while idx < len(self.data) and self.data[idx]:
            res += self.data[idx],
            idx += 1
        self.ptr = idx + 1
        return res
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)
