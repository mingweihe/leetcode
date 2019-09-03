class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        maxi = mini = res = nums[0]
        for i in xrange(1, len(nums)):
            temp = maxi
            maxi = max(maxi*nums[i], mini*nums[i], nums[i])
            mini = min(temp*nums[i], mini*nums[i], nums[i])
            res = max(res, maxi)
        return res
