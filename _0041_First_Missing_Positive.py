class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        bucket kind of sort
        1. recurrently arrange number to its correct position
        2. loop array to find the first missing number
        3. otherwise return length of array plus one
        """
        L = len(nums)
        for i in xrange(L):
            while 0 < nums[i] < L+1 and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        for i, x in enumerate(nums):
            if x != i+1: return i+1
        return L+1
