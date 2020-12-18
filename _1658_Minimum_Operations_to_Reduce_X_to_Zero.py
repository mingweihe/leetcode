class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        target = sum(nums) - x
        d = {0: -1}
        accum = 0
        res = -1
        for i, num in enumerate(nums):
            accum += num
            d[accum] = i
            if accum - target in d:
                res = max(res, i - d[accum-target])
        return -1 if res == -1 else len(nums) - res
