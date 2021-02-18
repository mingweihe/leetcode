class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## Approach 2
        a, b = 0, 0
        for x in nums:
            if x >= b: a, b = b, x
            elif x > a: a = x
        return (a-1) * (b-1)
    
        ## Approach 1
        # res = 0
        # for i in xrange(len(nums)-1):
        #     for j in xrange(i+1, len(nums)):
        #         res = max(res, (nums[i]-1) * (nums[j]-1))
        # return res
