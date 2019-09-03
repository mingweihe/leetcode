class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        first_small = -1
        for i in xrange(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                first_small = i
                break
        if first_small == -1:
            nums.reverse()
            return
        first_large = -1
        for i in xrange(len(nums) - 1, first_small, -1):
            if nums[i] > nums[first_small]:
                first_large = i
                nums[i], nums[first_small] = nums[first_small], nums[i]
                break

        left, right = first_small + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1
