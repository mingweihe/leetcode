class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #  Approach 2
        if not nums: return 0
        for i in range(1,len(nums)):
            if nums[i]: nums[i]+=nums[i-1]
        return max(nums)

        # Approach 1
        # first = -1
        # maximum = 0
        # for i in range(len(nums)):
        #     if nums[i] == 0: first = i
        #     else: maximum=max(maximum, i-first)
        # return maximum
