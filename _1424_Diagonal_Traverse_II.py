from collections import defaultdict


class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        # Approach 2
        d = defaultdict(list)
        m, n = len(nums), max(map(len, nums))
        for i in xrange(m):
            for j, x in enumerate(nums[i]):
                d[i+j] += x,
        res = []
        for i in xrange(m+n-1):
            cur = d[i][::-1]
            res += cur
        return res

        # Approach 1, brute force, O(m*n)
        # res = []
        # m, n = len(nums), max(map(len, nums))
        # out_coords = [[i, 0] for i in xrange(m)] + [[m-1, i] for i in xrange(1, n)]
        # for x, y in out_coords:
        #     i, j = x, y
        #     while i >= 0 and j < n:
        #         if j < len(nums[i]):
        #             res += nums[i][j],
        #         i -= 1
        #         j += 1
        # return res
