class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        A, L = sorted(nums), len(nums)
        B = [i for i in xrange(L) if A[i] != nums[i]]
        if not B: return 0
        return B[-1] - B[0] + 1
