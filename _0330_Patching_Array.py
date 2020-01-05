class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        missed, added, i = 1, 0, 0
        while missed <= n:
            if i < len(nums) and nums[i] <= missed:
                missed += nums[i]
                i += 1
            else:
                added += 1
                missed += missed
        return added
