class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Approach 1
        return len(nums) != len(set(nums))
        # Approach 2
        # d = {}
        # for i in nums:
        #     if i in d: return True
        #     d[i] = 0
        # return False
