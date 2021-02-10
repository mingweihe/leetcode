class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.sort(reverse=True)
        nums += float('-inf'),
        for i in xrange(n):
            if nums[i] >= i+1 and nums[i+1] < i+1:
                return i+1
        return -1
