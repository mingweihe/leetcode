class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Approach 2
        return len(nums) != len(set(nums))

        # Approach 1
        # d = {}
        # for i in nums:
        #     if i in d: return True
        #     d[i] = 0
        # return False
