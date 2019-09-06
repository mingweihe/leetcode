class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        tail_index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[tail_index]:
                tail_index += 1
                nums[tail_index] = nums[i]
        return tail_index + 1
