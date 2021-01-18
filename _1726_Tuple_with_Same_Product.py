from collections import defaultdict


class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n, d = len(nums), defaultdict(int)
        res = 0
        for i in xrange(1, n):
            for j in xrange(i):
                cur = nums[i] * nums[j]
                res += d[cur] * 8
                d[cur] += 1
        return res
