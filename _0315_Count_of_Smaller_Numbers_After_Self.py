class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
            Segment tree, append result when building the tree
            size of tree is relative with number of distinct values
        """
        res = []
        d = {v: i for i, v in enumerate(sorted(set(nums)))}
        L = self.L = len(d)
        tree = self.tree = [0] * (L << 1)
        for i in xrange(len(nums) - 1, -1, -1):
            res.append(self.range_sum(0, d[nums[i]] - 1))
            self.update(d[nums[i]], 1)
        return res[::-1]

    def update(self, i, val):
        i += self.L
        tree = self.tree
        tree[i] += val
        while i > 1:
            tree[i >> 1] = tree[i] + tree[i ^ 1]
            i >>= 1

    def range_sum(self, i, j):
        i += self.L
        j += self.L
        tree = self.tree
        res = 0
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
