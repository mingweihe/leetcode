class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        N, first_smaller = len(nums), -1
        for i in xrange(N-2, -1, -1):
            if nums[i] < nums[i+1]:
                first_smaller = i
                break
        if first_smaller == -1: 
            nums.reverse()
            return
        for i in xrange(N-1, first_smaller, -1):
            if nums[i] > nums[first_smaller]:
                nums[i], nums[first_smaller] = nums[first_smaller], nums[i]
                break
        l, r = first_smaller + 1, N - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
