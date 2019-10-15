class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Approach 1 time O(n*log(n)) space O(n)
        A = sorted(nums)
        idx, L = 0, len(nums)
        mid = (L-1) / 2
        for i in xrange(mid+1):
            nums[idx] = A[mid-i]
            if idx + 1 < L: nums[idx+1] = A[L-1-i]
            idx += 2
