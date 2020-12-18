import collections


class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        d = collections.defaultdict(int)
        for x in nums:
            if d[k-x]:
                res += 1
                d[k-x] -= 1
            else: d[x] += 1
        return res
