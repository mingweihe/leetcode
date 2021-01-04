class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted([[x, i] for i, x in enumerate(nums)])
        res = [0] * len(nums)
        for j, (x, i) in enumerate(nums):
            if j == 0:
                continue
            if x == nums[j-1][0]:
                res[i] = res[nums[j-1][1]]
                continue
            res[i] = j
        return res
