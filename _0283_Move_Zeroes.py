class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Approach 2
        j = 0
        for i in nums:
            if i:
                nums[j] = i
                j += 1
        nums[j:] = [0]*(len(nums)-j)

        # Approach 1
        # j = 0
        # for i in range(len(nums)):
        #     if nums[i]:
        #         nums[i], nums[j] = 0, nums[i]
        #         j += 1
