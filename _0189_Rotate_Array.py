class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l
        self.reverse(nums, 0, l - k - 1)
        self.reverse(nums, l - k, l - 1)
        self.reverse(nums, 0, l - 1)

    def reverse(self, nums, left, right):
        while left < right:
            t = nums[left]
            nums[left] = nums[right]
            nums[right] = t
            left += 1
            right -= 1
