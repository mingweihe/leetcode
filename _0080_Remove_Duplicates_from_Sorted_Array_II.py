class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        1 1 2 3 3
        """
        tail = 2  # tail is index which is to be modified
        for i in xrange(2, len(nums)):
            if nums[i] != nums[tail-2]:
                nums[tail] = nums[i]
                tail += 1
        return tail
