class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
            n dimensional segment tree
        """
        n = self.L = 0 if not matrix else len(matrix[0])
        m = len(matrix)
        trees = self.trees = []
        for i in xrange(m):
            tree = [0]*n + matrix[i]
            for i in xrange(n-1, 0, -1):
                tree[i] = tree[i<<1] + tree[i<<1|1]
            trees += tree,

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: None
        """
        col += self.L
        tree = self.trees[row]
        tree[col] = val
        while col > 1:
            tree[col>>1] = tree[col] + tree[col^1]
            col >>= 1

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        res = 0
        for i in xrange(row1, row2+1):
            tree = self.trees[i]
            i, j = self.L + col1, self.L + col2
            while i <= j:
                if i & 1:
                    res += tree[i]
                    i += 1
                if j & 1 == 0:
                    res += tree[j]
                    j -= 1
                i >>= 1
                j >>= 1
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
