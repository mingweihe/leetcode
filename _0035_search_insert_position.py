class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Method 1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l += 1
            else:
                r -= 1
        return l

        # Method 2
        # if not nums: return 0
        # l, r = 0, len(nums) - 1
        # while True:
        #     mid = int((l + r) / 2)
        #     if target <= nums[0]:
        #         return 0
        #     elif target > nums[len(nums) - 1]:
        #         return len(nums)
        #     elif nums[mid] < target <= nums[mid + 1]:
        #         return mid + 1
        #     elif nums[mid - 1] < target <= nums[mid]:
        #         return mid
        #     elif nums[mid] >= target:
        #         r = mid - 1
        #     else:
        #         l = mid + 1
