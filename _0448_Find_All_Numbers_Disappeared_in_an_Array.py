class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Approach 1
        return list(set(range(1, len(nums)+1)) - set(nums))

        # Approach 2
        # for i in nums: nums[abs(i) - 1] = -abs(nums[abs(i) - 1])
        # return [i + 1 for i in range(len(nums)) if nums[i] > 0]
