class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
            typical segment tree solved puzzle
        """
        L = self.L = len(nums)
        tree = self.tree = [0]*L+nums
        for i in xrange(L-1, 0, -1):
            tree[i] = tree[i<<1] + tree[i<<1|1]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        i += self.L
        tree = self.tree
        tree[i] = val
        while i > 1:
            tree[i>>1] = tree[i] + tree[i^1]
            i >>= 1

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        i += self.L
        j += self.L
        res, tree = 0, self.tree
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


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
