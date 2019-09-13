class Vector2D(object):

    def __init__(self, v):
        """
        :type v: List[List[int]]
            # Approach 1 d vector
            # Approach 2 2d vector with indices of current row and col
            # Approach 3 java / c++ iterator
        """
        self.index_row = 0
        self.index_col = 0
        self.v = v

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            res = self.v[self.index_row][self.index_col]
            self.index_col += 1
            return res

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.index_row < len(self.v):
            if self.index_col < len(self.v[self.index_row]):
                return True
            else:
                self.index_row += 1
                self.index_col = 0
        return False

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
