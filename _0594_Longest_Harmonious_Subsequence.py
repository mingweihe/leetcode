import collections


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, d, s = 0, collections.Counter(nums), set(nums)
        for i in s:
            if i+1 in d: res = max(res, d[i+1]+d[i])
        return res
