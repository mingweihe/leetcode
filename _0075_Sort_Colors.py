class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        r, i, b = 0, 0, len(nums) - 1
        while i <= b:
            if nums[i] == 0:
                self.swap(nums, i, r)
                i += 1
                r += 1
            elif nums[i] == 2:
                self.swap(nums, i, b)
                b -= 1
            else:
                i += 1

    def swap(self, nums, l, r):
        t = nums[l]
        nums[l] = nums[r]
        nums[r] = t
