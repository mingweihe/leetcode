class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in xrange(1, len(nums)):
            if i & 1 and nums[i] < nums[i - 1] or not i & 1 and nums[i] > nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
