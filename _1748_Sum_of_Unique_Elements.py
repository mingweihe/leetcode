from collections import Counter


class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(k for k, v in Counter(nums).items() if v == 1)
