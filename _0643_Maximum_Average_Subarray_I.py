import numpy as np


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Approach 2
        cums = np.cumsum([0] + nums)
        return max(cums[k:] - cums[:-k]) / float(k)

        # Approach 1
        # M = sum(nums[:k])
        # cur = M
        # for i, x in enumerate(nums[k:]):
        #     cur = cur-nums[i]+x
        #     M = max(M, cur)
        # return float(M)/k
