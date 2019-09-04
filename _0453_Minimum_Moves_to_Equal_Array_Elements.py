class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach 2
        return sum(nums) - len(nums) * min(nums)

        # Approach 1
        # m = min(nums)
        # return sum(i - m for i in nums)

