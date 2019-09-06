class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach 2
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] = nums[i] + nums[i-1]
        return max(nums)

        # Approach 1
        # if len(nums) == 1: return nums[0]
        # return self.dfs(nums, 1, nums[0])

    # def dfs(self, nums, index, accum):
    #     if len(nums) - 1 == index:
    #         return max(accum, accum + nums[index], nums[index])
    #     if accum < 0:
    #         return max(accum, self.dfs(nums, index + 1, nums[index]))
    #     return max(accum, self.dfs(nums, index + 1, nums[index] + accum))
