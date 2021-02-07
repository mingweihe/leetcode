class SubrectangleQueries(object):

    def __init__(self, rectangle):
        """
        :type rectangle: List[List[int]]
        """
        ## Approach 2
        self.A = rectangle
        self.updates = []
        
        ## Approach 1
        # self.A = rectangle

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :type newValue: int
        :rtype: None
        """
        ## Approach 2
        self.updates += [row1, col1, row2, col2, newValue],
        
        ## Approach 1
        # for i in xrange(row1, row2+1):
        #     for j in xrange(col1, col2+1):
        #         self.A[i][j] = newValue

    def getValue(self, row, col):
        """
        :type row: int
        :type col: int
        :rtype: int
        """
        ## Approach 2
        for i in xrange(len(self.updates)-1, -1, -1):
            r1, c1, r2, c2, val = self.updates[i]
            if r1 <= row <= r2 and c1 <= col <= c2:
                return val        
        return self.A[row][col]
    
        ## Approach 1
        # return self.A[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
