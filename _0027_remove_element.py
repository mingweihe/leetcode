class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Approach 1
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == val:
                cnt += 1
            else:
                nums[i - cnt] = nums[i]
        return len(nums) - cnt

        # Approach 2
        # if not nums: return 0
        # tail_index = len(nums) - 1
        # for i in range(len(nums)-1, -1, -1):
        #     if nums[i] == val:
        #         t = nums[i]
        #         nums[i] = nums[tail_index]
        #         nums[tail_index] = t
        #         tail_index -= 1
        # return tail_index + 1


