class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach 1
        return len(nums)*(1+len(nums))/2 - sum(nums)
        # Approach 2
        # return sum(range(len(nums) + 1)) - sum(nums)
