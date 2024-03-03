class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a1, a2 = [nums[0]], [nums[1]]
        for i in xrange(2, len(nums)):
            if a1[-1] > a2[-1]:
                a1 += nums[i],
            else:
                a2 += nums[i],
        return a1 + a2
