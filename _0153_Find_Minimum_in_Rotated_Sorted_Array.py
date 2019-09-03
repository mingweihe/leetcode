class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        7,0,1,2,4,5,6
        5,6,7,0,1,2,4
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) / 2
            if nums[m] >= nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l - 1]
